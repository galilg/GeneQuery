CREATE CONSTRAINT ON (p:Patient) ASSERT p.patient_id IS UNIQUE;

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///patients.csv' AS line WITH line

MERGE (person:Patient {patient_id: line.patient_id })

MERGE (g:Gender {gender: line.gender })

CREATE (person)-[:is_a]->(g);
