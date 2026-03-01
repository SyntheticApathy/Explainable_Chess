# Get facts from the ontology, once it's been created.
# More of a place holder for now, might be removed in favour of llm-generated queries.



def get_basic_description(onto):
    # This query finds all pieces, their squares, and what they attack/defend
    base_iri = onto.base_iri
    
    query = f"""
    PREFIX : <{base_iri}>
    SELECT DISTINCT ?piece ?property ?target
    WHERE {{
        ?piece rdf:type/rdfs:subClassOf* :Piece .
        ?piece ?property ?target .
        FILTER(?property IN (:onSquare, :isAttacking, :isDefending, :legalMove, :onSquare))
    }}
    """
    results = list(onto.world.sparql(query))
    return results