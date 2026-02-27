from upload_info_to_ontology import _input
from get_facts import get_basic_description
from llm import basic


#This file runs the pipeline.

facts = get_basic_description(_input())
print(basic(facts,evaluation=1))