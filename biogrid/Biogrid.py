#---- Imports -----------------------------------------------------------------

from neo4j.v1 import GraphDatabase, basic_auth

import pandas as pd


#---- Public Classes ----------------------------------------------------------

class Biogrid(object):
    def __init__(self):
        return None


    def connect_two_genes(self, tx, gene_a, gene_b):
        tx.run("MERGE (a:Gene {entrez_id: $id_a})"
               "MERGE (a)-[:INTERACTS_WITH]->(b:Gene {entrez_id: $id_b})",
               id_a=gene_a, id_b=gene_b)


    def print_gene_names(self, tx, gene_id):
        for record in tx.run("MATCH (a:Gene)-[:INTERACTS_WITH]->(gene_b) \
                              WHERE a.entrez_id = $a_id "
                             "RETURN gene_b.entrez_id", a_id=gene_id):
            print(record["gene_b.entrez_id"])


    def start_session(self):
        driver = GraphDatabase.driver("bolt://localhost:7687",
                                            auth=basic_auth("neo4j", "optiplex")
                                          )
        session = driver.session()
        return session


#---- Main --------------------------------------------------------------------

driver = GraphDatabase.driver("bolt://localhost:7687",
                               auth=basic_auth("neo4j", "optiplex"))
session = driver.session()

biogrid = Biogrid()

biogrid.connect_two_genes(session, '10999', '90634')

biogrid.print_gene_names(session, '10999')


session.close()
#session.run("CREATE (a:Person {name: {name}, title: {title}})",
#            {"name": "Arthur", "title": "King"})
#
#result = session.run("MATCH (a:Person) WHERE a.name = {name} "
#                     "RETURN a.name AS name, a.title AS title",
#                     {"name": "Arthur"})
#
#for record in result:
#    print("{} {}" .format(record["title"], record["name"]))

