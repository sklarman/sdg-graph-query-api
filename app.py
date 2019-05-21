from flask import Flask, request, abort
from SPARQLWrapper import SPARQLWrapper, JSON, BASIC
import json


app = Flask(__name__)

GRAPHDB = "http://35.231.89.123:7200/repositories/sdgs"
QUERY = """
PREFIX sdgo: <http://data.un.org/ontology/sdg#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX : <http://data.un.org/ontology/sdg#>
PREFIX schema: <http://schema.org/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?concept ?conceptBroader ?entityBroader ?typeLabel ?entityLabel WHERE {
    VALUES ?concept { %s }
    
    ?concept skos:broader* ?conceptBroader .
    ?entity dct:subject ?conceptBroader .
    ?entity skos:broader* ?entityBroader .
    
    ?entityBroader rdf:type ?type .
    FILTER (CONTAINS(str(?type), "ontology/sdg"))
    ?type rdfs:label ?typeName .
    ?entityBroader skos:prefLabel ?entityName .
    
    BIND(STR(?typeName) as ?typeLabel)
    BIND(STR(?entityName) as ?entityLabel)
}
"""


@app.route('/')
def index():
    return "This is a graph query API!"

@app.route('/api', methods=['POST'])
def get_related_entities():
    input_matches = request.get_json()
    concept_index = set()
    for match in input_matches:
        url = match["url"]
        concept_index.add(url)
    values_string = ""
    for uri in concept_index:
        value_string = "<" + uri + "> "
        values_string = values_string + value_string
    sparql_query = QUERY % values_string
    sparql_results = get_sparql_results(sparql_query) 
    final_index = {}
    for result in sparql_results['results']['bindings']:
        final_index = process_sparql_result(result, final_index)

    return json.dumps(final_index), 200, {'Content-Type': 'application/json'}

def get_sparql_results(sparql_query):
    sparql = SPARQLWrapper(GRAPHDB)
    sparql.setHTTPAuth(BASIC)
    sparql.setCredentials("sdg-guest", "lod4stats")
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def process_sparql_result(result, index):
    entity = result["entityBroader"]["value"]
    concept = result["concept"]["value"]
    concept_intermediate = result["conceptBroader"]["value"]
    type_label = result["typeLabel"]["value"]
    entity_label = result["entityLabel"]["value"]
    
    if entity in index:
        ent_index = index[entity]
        ent_index["count"] += 1
        if concept in ent_index["concept"]:
            ent_index["concept"][concept]["count"] += 1
        else:
            ent_index["concept"][concept] = {
                "count": 1,
                "intermediate": []
            }
            
    else:
        index[entity] = {
            "count": 1,
            "type": type_label, 
            "label": entity_label,
            "concept": {
                concept: {
                    "count": 1,
                    "intermediate": []
                }
            }
        }
    
    if concept_intermediate != concept and concept_intermediate not in ent_index["concept"][concept]["intermediate"]:
            ent_index["concept"][concept]["intermediate"].append(concept_intermediate)
    
    return index

if __name__ == '__main__':
    app.run(debug=True)
