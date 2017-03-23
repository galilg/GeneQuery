#!/usr/bin/python3 /usr/bin/env

CREATE CONSTRAINT ON (g:Gene) ASSERT g.entrez_id IS UNIQUE;


USING PERIODIC COMMIT 200
LOAD CSV WITH HEADERS FROM
'file:///BIOGrid2.csv' AS line
WITH line

MERGE (gene_a:Gene {entrez_id: TOINT(line.`Entrez Gene Interactor A`) })

MERGE (gene_b:Gene {entrez_id: TOINT(line.`Entrez Gene Interactor B`) })

CREATE (gene_a)-[:interacts]->(gene_b);
