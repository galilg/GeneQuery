#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

from Biogrid import Biogrid

from neo4j.v1 import GraphDatabase, basic_auth

#---- Main --------------------------------------------------------------------

driver = GraphDatabase.driver("bolt://127.0.0.1:7687",
                              auth=basic_auth(
                                    "neo4j",
                                    "optiplex"))

session = driver.session()

bGrid = Biogrid()
result = bGrid.get_n_degree_interacting_genes(session, 586, 3)
bGrid.add_entry(session, 'HYETHERE')
print("result: ", result)
