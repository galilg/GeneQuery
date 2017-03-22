#---- Imports -----------------------------------------------------------------

from neo4j.v1 import GraphDatabase, basic_auth

import pandas as pd


#---- Public Classes ----------------------------------------------------------

class Biogrid(object):
    def __init__(self):
        return None


    def connect_two_genes(self, tx, gene_a, gene_b):

        tx.run("CREATE (a:Gene {entrez_id: $id_a})"
               "CREATE (b:Gene {entrez_id: $id_b})"
               "CREATE (a)-[:INTERACTS_WITH]->(b)",
               id_a=gene_a, id_b=gene_b)



    def print_gene_names(self, tx, gene_id):
        for record in tx.run("MATCH (a:Gene)-[:INTERACTS_WITH]->(gene_b) \
                              WHERE a.entrez_id = $a_id "
                             "RETURN gene_b.entrez_id", a_id=gene_id):
            print(record["gene_b.entrez_id"])


