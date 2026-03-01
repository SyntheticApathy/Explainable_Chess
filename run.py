from upload_info_to_ontology import _input
from get_facts import get_basic_description
from llm import basic
from chess_logic import get_eval


#This file runs the pipeline.

print(get_basic_description(_input()))
