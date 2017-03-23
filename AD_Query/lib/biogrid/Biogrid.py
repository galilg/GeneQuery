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
               "CREATE (a)-[:interacts]->(b)",
               id_a=gene_a, id_b=gene_b)


    def get_n_degree_interacting_genes(self, gene, n):
        tx.run("MATCH (:Gene)-[:interacts*..$degrees]->(b:Gene) "
               "WHERE b.enterez_id = $gene_id "
               "RETURN b",
               degrees=n, gene_id=gene)


    def convert_biogrid_to_csv(self, file_path):
        df = pd.read_csv(file_path, 'r', sep=('\t'), header=(0))
        df.to_csv(out_file_path, sep=',')


    def load_biogrid_csv(self, file_path):
        tx.run("CREATE CONSTRAINT ON (g:Gene) ASSERT g.entrez_id IS UNIQUE; "
               "USING PERIODIC COMMIT 200 "
               "LOAD CSV WITH HEADERS FROM "
               "'file://$file_path AS line "
               " WITH line "
               "MERGE (gene_a:Gene {entrez_id: TOINT(line.`Entrez Gene Interactor A`) }) "
                "MERGE (gene_b:Gene {entrez_id: TOINT(line.`Entrez Gene Interactor B`) }) "
                "CREATE (gene_a)-[:interacts]->(gene_b); ",
                file_path=file_path )


    def print_gene_names(self, tx, gene_id):
        for record in tx.run("MATCH (a:Gene)-[:INTERACTS_WITH]->(gene_b) \
                              WHERE a.entrez_id = $a_id "
                             "RETURN gene_b.entrez_id", a_id=gene_id):
            print(record["gene_b.entrez_id"])


