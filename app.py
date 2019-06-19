from flask import Flask, request, abort
from SPARQLWrapper import SPARQLWrapper, JSON, BASIC
import json
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://34.66.148.181:3000"}})

GRAPHDB = "http://34.66.148.181:7200/repositories/sdgs"
QUERY = """
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <http://schema.org/>
SELECT ?concept ?conceptBroader ?entity ?typeLabel ?entityLabel WHERE {
    VALUES ?concept { %s }
    
    ?concept skos:broader* ?conceptBroader .
    ?entity dct:subject ?conceptBroader .    
    
    ?entity rdf:type ?type .
    FILTER (CONTAINS(str(?type), "ontology/sdg"))
    ?type rdfs:label ?typeName .
    ?entity skos:prefLabel ?entityName .
    OPTIONAL {
    ?entity schema:description ?entityDescription .
    }

    BIND(STR(?typeName) as ?typeLabel)
    BIND(COALESCE(STR(?entityDescription), STR(?entityName)) as ?entityLabel)
}
"""


# ?concept skos:broader* ?conceptBroader .
#     ?entityLow dct:subject ?conceptBroader .
#     ?entityLow skos:broader* ?entity .
#     ?entity dct:subject ?conceptBroader .
    
@app.route('/')
def index():
    return "This is graph query API!"

@app.route('/api', methods=['POST'])
@cross_origin()
def get_related_entities():
    input_matches = request.get_json()
    concept_index = {}
    for match in input_matches:
        concept_index = extend_concept_index(match, concept_index)
    values_string = ""
    entities_results = {}
    counter = 0
    for uri in concept_index:
        counter += 1
        value_string = "<" + uri + "> "
        values_string = values_string + value_string
        if (counter % 50 == 0) or counter == len(concept_index):
            print(counter)
            sparql_query = QUERY % values_string
            sparql_results_entities = get_sparql_results(sparql_query) 
            for result in sparql_results_entities['results']['bindings']:
                entities_results = process_sparql_result(result, entities_results, concept_index)
            values_string = ""

    return json.dumps(entities_results), 200, {'Content-Type': 'application/json'}

def get_sparql_results(sparql_query):
    sparql = SPARQLWrapper(GRAPHDB)
    sparql.setHTTPAuth(BASIC)
    sparql.setCredentials("sdg-guest", "lod4stats")
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results


def process_sparql_result(result, index, concept_index):
    entity = result["entity"]["value"]
    concept = result["concept"]["value"]
    type_label = result["typeLabel"]["value"]
    entity_label = result["entityLabel"]["value"]

    weight = concept_index[concept]
    if type_label=="Goal":
        weight = weight * 3
    if type_label=="Target":
        weight = weight * 1.3
    if type_label=="Indicator":
        weight = weight * 1.1

    if entity in index:
        ent_index = index[entity]
        if concept in ent_index["concept"]:
            ent_index["concept"][concept]["weight"] += weight
        else:
            ent_index["concept"][concept] = {
                "weight": weight
            }
    else:
        index[entity] = {
            "type": type_label, 
            "label": entity_label,
            "concept": {
                concept: {
                    "weight": weight
                }
            }
        }
    
    # if concept_intermediate != concept and concept_intermediate not in ent_index["concept"][concept]["intermediate"]:
    #         ent_index["concept"][concept]["intermediate"].append(concept_intermediate)
    
    return index


def extend_concept_index(match, concept_index):
    url = match["url"]
    weight = 1
    if 'weight' in match:
        weight = match["weight"]
    if url in concept_index:
        concept_index[url] += weight
    else:
        concept_index[url] = weight
    return concept_index


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=False)
