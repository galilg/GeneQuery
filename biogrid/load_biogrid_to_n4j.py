#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

from Biogrid import Biogrid
from neo4j.v1 import GraphDatabase, basic_auth

import pandas as pd

#---- Functions ---------------------------------------------------------------

def load_biogrid_file(file_location='../../BIOGRID-MV-Physical-3.4.144.tab2'):
    biogrid_df = pd.read_csv(file_location, sep='\t', header=(0))
    return biogrid_df


#---- Open Session ------------------------------------------------------------

#driver = GraphDatabase.driver("bolt://localhost:7687",
#                              auth=basic_auth("neo4j", "optiplex"))
#session = driver.session()

#---- Main --------------------------------------------------------------------

biogrid = Biogrid()
df = load_biogrid_file()
length_of_df = len(df)
#for row in range(0, length_of_df):
#    print(row)
#print(df.iloc[0]['Entrez Gene Interactor A'])
#print(len(df))
for row in range(0, length_of_df):
    driver = GraphDatabase.driver("bolt://localhost:7687",
                              auth=basic_auth("neo4j", "optiplex"))
    session = driver.session()
    #import pdb; pdb.set_trace()
    gene_a = df.iloc[row]['Entrez Gene Interactor A']
    gene_b = df.iloc[row]['Entrez Gene Interactor B']
    biogrid.connect_two_genes(session, str(gene_a), str(gene_b))

#    print(row)
#biogrid.print_gene_names(session, '10999')


#---- Close Session -----------------------------------------------------------

#session.close()
