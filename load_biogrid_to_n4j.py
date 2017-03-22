#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

from Biogrid import Biogrid
from neo4j.v1 import GraphDatabase, basic_auth

import pandas as pd

#---- Functions ---------------------------------------------------------------

def load_biogrid_file(file_location='../BIOGRID-MV-Physical-3.4.144.tab2'):
    biogrid_df = pd.read_csv(file_location, sep='\t', header=(0))
    return biogrid_df


def start_session(bolt_port='bolt://localhost:7687',
                  username='neo4j',
                  password='optiplex'):
    driver = GraphDatabase.driver(bolt_port,
                                  auth=basic_auth(username, password))
    session = driver.session()
    return session


#---- Open Session ------------------------------------------------------------

driver = GraphDatabase.driver("bolt://localhost:7687",
                               auth=basic_auth("neo4j", "optiplex"))
session = driver.session()


#---- Main --------------------------------------------------------------------

biogrid = Biogrid()
df = load_biogrid_file()

print(df.iloc[0]['Entrez Gene Interactor A'])
biogrid.connect_two_genes(session, '10999', '90634')

biogrid.print_gene_names(session, '10999')


#---- Close Session -----------------------------------------------------------

session.close()
