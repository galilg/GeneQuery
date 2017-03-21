#!/usr/bin/env

#---- Imports -----------------------------------------------------------------

import csv
import pandas as pd
import math
import numpy as np

from cassandra.cluster import Cluster

#---- Functions ---------------------------------------------------------------

def create_cql_keyspace(keyspace_name):
    cluster = Cluster()
    session = cluster.connect()
    key = session.execute("""
                          CREATE KEYSPACE IF NOT EXISTS {}
                          WITH replication = {{ 'class': 'SimpleStrategy',
                                               'replication_factor': 3}};
                          """ .format(keyspace_name))



def get_headers(rosmap):
    #import pdb; #pdb.set_trace()
    header_values = list(rosmap.columns.values)
    header_values = header_values[2:]
    headers_with_types = []
    headers_without_types = []
    headers_with_types.append('PATIENT_ID text PRIMARY KEY')
    headers_with_types.append('DIAGNOSIS double')
    headers_without_types.append('PATIENT_ID')
    headers_without_types.append('DIAGNOSIS')

    for vals in header_values:
        headers_without_types.append('entrez_id_' + str(vals))
        headers_with_types.append('entrez_id_' + str(vals) + ' double')
    #headers_without_type('entrez_id_' + str(header_values[-1]))
    #headers_with_types += (', entrez_id_' + str(header_values[-1]) + ' double')
    #import pdb; #pdb.set_trace()
    return (headers_with_types, headers_without_types)


def load_data_file(file):
    rosmap =  pd.read_csv(file)
    rosmap = rosmap.replace(np.nan, -1.0)
    return rosmap


def create_table(headers, keyspace_name, table_name):
    cluster = Cluster()
    session = cluster.connect(keyspace_name)
    headers = ', '.join(headers)
    session.execute("""
                    CREATE TABLE IF NOT EXISTS {} ({});
                    """.format(table_name, headers))


def get_insert_db_line(row):
    line_to_insert = []
    line_to_insert.append(row[0])
    for item in enumerate(row[1:]):
        line_to_insert.append(item[1])
    return line_to_insert


def populate_table(headers_without_types, keyspace_name, rosmap, table_name):
    cluster = Cluster()
    session = cluster.connect(keyspace_name)
    headers_without_types = ', '.join(headers_without_types)
    #import pdb; pdb.set_trace()
    for entry in range(1, len(rosmap.index)):
        insert_line = get_insert_db_line(rosmap.loc[entry])
        line = ', '.join(str(v) for v in insert_line)
        patient_id = "'"+line[0:11] +"'"
        line = line[11:]
        concat = patient_id + line
        session.execute("""
                        INSERT INTO {}({})
                        VALUES ({}{})
                        """.format(table_name,
                                   headers_without_types,
                                   patient_id,
                                   concat)
                        )


#---- Main --------------------------------------------------------------------

file = '../ROSMAP_RNASeq_entrez.csv'
keyspace_name = 'rosmap_rna'
table_name = 'patient_diagnosis'
rosmap = load_data_file(file)
headers_with_types, headers_without_types = get_headers(rosmap)
create_cql_keyspace(keyspace_name)
#import pdb; #pdb.set_trace()
create_table(headers_with_types, keyspace_name, table_name)
populate_table(headers_without_types, keyspace_name, rosmap, table_name)


