from flask import Flask, request, abort, Response
from SPARQLWrapper import SPARQLWrapper, JSON, BASIC
import json
import csv
import copy
import requests
from requests.auth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
from pyld import jsonld


app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://34.66.148.181:3000"}})

GRAPHDB = "http://34.66.148.181:7200/repositories/sdgs"
QUERY = """
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <http://schema.org/>
SELECT ?concept ?conceptBroader ?entity ?typeLabel WHERE {
    VALUES ?concept { %s }
    
    ?concept skos:broader* ?conceptBroader .
    ?entity dct:subject ?conceptBroader .   

    
    ?entity rdf:type ?type .
    FILTER (CONTAINS(str(?type), "ontology/sdg"))
    ?type rdfs:label ?typeName .

    BIND(STR(?typeName) as ?typeLabel)
}
"""

STAT_QUERY = """
PREFIX sdgo: <http://data.un.org/ontology/sdg#>
CONSTRUCT {
    ?x ?p ?o
} WHERE {

    VALUES ?country { %s }

    GRAPH <http://data.un.org/series/sdg> {
    
        ?x sdgo:fromSeries <%s> .
        ?x sdgo:ISO3CD ?country .
        ?x ?p ?o .
        FILTER(?p!=sdgo:fromSeries)

    }
}
"""

with open('response-template.json', encoding="utf-8") as f:
    response_template = json.load(f)

concept_index_main = {}

concept_index_source = csv.DictReader(open("concept-index.tsv", encoding="utf8"), delimiter="\t")
for concept in concept_index_source:
    concept_index_main[concept["id"]] = {
        "url": concept["id"],
        "label": concept["label"],
        "source": concept["source"]
    }

# ?concept skos:broader* ?conceptBroader .
#     ?entityLow dct:subject ?conceptBroader .
#     ?entityLow skos:broader* ?entity .
#     ?entity dct:subject ?conceptBroader .
    

def merge(source, target):
    for key in source:
        target[key] = source[key]
        if key == 'value':
            target[key] = round(target[key])

    return target

def get_final_result(entities):

    resp = copy.deepcopy(response_template)
    
    goals = []

    for goal in resp["children"]:
        if goal["id"] in entities:
            goal_entity = entities[goal["id"]]
            goal_entity["name"] = goal["name"]

            targets = []

            for target in goal["children"]:
                if target["id"] in entities:
                    target_entity = entities[target["id"]]
                    target_entity["name"] = target["name"]

                    indicators = []

                    for indicator in target["children"]:
                        if indicator["id"] in entities:
                            indicator_entity = entities[indicator["id"]]
                            indicator_entity["name"] = indicator["name"]
                            

                            serieses = []

                            for series in indicator["children"]:
                                if series["id"] in entities:
                                    series_entity = entities[series["id"]]
                                    series_entity["name"] = series["name"]

                                    new_series = merge(series_entity, series)

                                    if new_series["value"] > 2:
                                        serieses.append(new_series)

                            indicator["children"] = serieses

                            new_indicator = merge(indicator_entity, indicator)
                    
                            if new_indicator["value"] > 2  or len(serieses)>0:
                                indicators.append(new_indicator)

                    target["children"] = indicators

                    new_target = merge(target_entity, target)
            
                    if new_target["value"] > 2 or len(indicators)>0:
                        targets.append(new_target)

            goal["children"] = targets

            new_goal = merge(goal_entity, goal)
            
            if new_goal["value"] > 2  or len(targets)>0:
                goals.append(new_goal)

    resp["children"] = goals

    return resp





@app.route('/')
def index():
    return "This is graph query API!"

@app.route('/stats', methods=['POST'])
@cross_origin()
def get_related_stats():
    input_params = request.get_json()
    countries = "\"" + ("\" \"").join(input_params["countries"]) + "\""
    stat = input_params["stat"]
    query = STAT_QUERY % (countries, stat)
    response = requests.get(GRAPHDB, auth=('sdg-guest', 'lod4stats'), params={"query":query}, headers={"Accept":"application/ld+json"})
    
    doc = {'@context': { '@vocab': 'http://data.un.org/ontology/sdg#'}, '@graph': json.loads(response.content) }
    flattened = jsonld.flatten(doc, { '@vocab': 'http://data.un.org/ontology/sdg#'})
    return Response(json.dumps(flattened["@graph"]), mimetype='application/json') 


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

    result = get_final_result(entities_results)

    return json.dumps(result), 200, {'Content-Type': 'application/json'}

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
    broader = result["conceptBroader"]["value"]
    type_label = result["typeLabel"]["value"]

    weight = concept_index[concept]
    if type_label=="Goal":
        weight = weight * 3
    if type_label=="Target":
        weight = weight * 1.3
    if type_label=="Indicator":
        weight = weight * 1.1

    if entity in index:
        ent_index = index[entity]
        ent_index["value"] += weight
        if broader in ent_index["concept"]:
            ent_index["concept"][broader]["value"] += weight
            if concept not in ent_index["concept"][broader]["subconcepts"]:
                ent_index["concept"][broader]["subconcepts"][concept] = concept_index_main[concept]
        else:
            ent_index["concept"][broader] = {
                "value": weight,
                "label": concept_index_main[broader]["label"],
                "url": concept_index_main[broader]["url"],
                "source": concept_index_main[broader]["source"],
                "subconcepts": { concept: concept_index_main[concept] }
            }
    else:
        index[entity] = {
            "type": type_label, 
            "value": weight,
            "concept": {
                broader: {
                    "value": weight,
                    "label": concept_index_main[broader]["label"],
                    "url": concept_index_main[broader]["url"],
                    "source": concept_index_main[broader]["source"],
                    "subconcepts": { concept: concept_index_main[concept] }
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
