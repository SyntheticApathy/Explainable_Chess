from upload_info_to_ontology import _input
from get_facts import get_basic_description
from llm import generate_explanation
from chess_logic import get_eval


#This file runs the pipeline.

facts = get_basic_description(_input())
print(facts)
#print(generate_explanation(facts,get_eval().get('value')))
