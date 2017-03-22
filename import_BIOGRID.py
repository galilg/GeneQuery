from neo4j.v1 import GraphDatabase, basic_auth
import pandas as pd

df = pd.read_csv('../BIOGRID-MV-Physical-3.4.144.tab2', sep='\t', header=(0))

driver = GraphDatabase.driver("bolt://localhost:7687",
                                    auth=basic_auth("neo4j", "optiplex")
                                  )
session = driver.session()

def connect_two_genes(gene_a, gene_b):
    result = session.run("CREATE (a:Gene {entrez_id: {gene_a}})",
                {"gene_a": gene_a})
    print("THE result: ", result.keys)
    session.run("CREATE (b:Gene {entrez_id: {gene_b}})",
                {"gene_b": gene_b})

    #session.run("CREATE (a)-[r:interacts_with]->(b) WHERE a.entrez_id = {id_a}\
    #             AND b.entrez_id = {id_b}",
    #             {"id_a": gene_a, "id_b": gene_b})


connect_two_genes('99999', '88888')


result = session.run("MATCH(a: Gene) RETURN a")#-[]->(b:Gene)"
                     #"RETURN a, b")

#for record in result:
#    print("This: ", record)

