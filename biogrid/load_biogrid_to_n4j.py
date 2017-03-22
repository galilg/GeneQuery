#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

from neo4j.v1 import GraphDatabase, basic_auth

import pandas as pd

#---- Public Classes ----------------------------------------------------------

class Biogrid(object):
    def __init__(self, file_location= \
                            '../../BIOGRID-MV-Physical-3.4.144.tab2'):
        self.biogrid_df = pd.read_csv(file_location, sep'\t', header=(0))

    def connect_two_genes(self, gene_a, gene_b):
        session = self.__start_session()
        session.run("CREATE (a:Gene {entrez_id: {{}}})".format(gene_a)
                    "CREATE (b:Gene {entrez_id: {{}}})".format(gene_b)
                    "CREATE (a)-[r:interacts_with]->(b)")

    def __start_session(self):
        driver = GraphDatabase.driver("bolt://localhost:7687",
                                            auth=basic_auth("neo4j", "optiplex")
                                          )
        session = driver.session()
        return session
#---- Main --------------------------------------------------------------------

driver = GraphDatabase.driver("bolt://localhost:7687",
                               auth=basic_auth("neo4j", "optiplex"))
session = driver.session()


session.run("CREATE (a:Person {name: {name}, title: {title}})",
            {"name": "Arthur", "title": "King"})

result = session.run("MATCH (a:Person) WHERE a.name = {name} "
                     "RETURN a.name AS name, a.title AS title",
                     {"name": "Arthur"})

for record in result:
    print("{} {}" .format(record["title"], record["name"]))

session.close()
