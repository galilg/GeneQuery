#!/usr/bin/env

import csv
import pandas as pd
from cassandra.cluster import Cluster

rosmap =  pd.read_csv('../ROSMAP_RNASeq_entrez.csv')

header_values = list(rosmap.columns.values)
header_values = header_values[2:]
headers_with_types = 'PATIENT_ID text PRIMARY KEY, DIAGNOSIS text'
headers_without_types = 'PATIENT_ID, DIAGNOSIS'

for vals in header_values:
    headers_without_types += (', ' + 'Entrez_id_' + str(vals))
    headers_with_types += (', ' + 'Entrez_id_' + str(vals) + ' double')


cleaned_rosmap = []
with open('../ROSMAP_RNASeq_entrez.csv', 'r') as infile:
    data = csv.reader(infile, delimiter=',')
    for line in data:
        clean_line = ''
        for word in line[:-1]:
            clean_line += (word + ', ')
        clean_line += line[-1]
        cleaned_rosmap.append(clean_line)

cluster = Cluster()
session = cluster.connect()
session.execute("""
                CREATE KEYSPACE IF NOT EXISTS rosmap_rna WITH REPLICATION = {
                    'class' : 'SimpleStrategy', 'replication_factor' : 3
                    };
                """)
session = cluster.connect('rosmap_rna')
session.execute("""
                CREATE TABLE IF NOT EXISTS patient_diagnosis( {} );
                """ .format(headers_with_types))
import pdb; pdb.set_trace()
for line in cleaned_rosmap[1:]:
    session.execute("""
                    INSERT INTO patient_diagnosis({})
                    VALUES ({})
                    """.format(headers_without_types, line))
#session.execute("""
#                COPY patient_diagnosis( {} )
#                FROM '../ROSMAP_RNASeq_entrez.csv'
#                WITH header='true'
#                """ .format(headers_without_types))

