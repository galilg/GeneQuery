#!/usr/bin/python3 /usr/bin/env

CREATE CONSTRAINT ON (g:Gene) ASSERT g.entrez_id IS UNIQUE;


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///patients.csv' AS line WITH line

MERGE (gene_a:Genes {entrez_id: TOINT(line.`Entrez Gene Interactor A`) })

MERGE (gene_b:Genes {entrez_id: TOINT(line.`Entrez Gene Interactor B`) })

CREATE (gene_a)-[:interacts]->(gene_b);
