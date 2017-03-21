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
    import pdb; pdb.set_trace()
    header_values = list(rosmap.columns.values)
    header_values = header_values[2:]
    headers_with_types = 'PATIENT_ID text PRIMARY KEY, DIAGNOSIS double'
    headers_without_types = 'PATIENT_ID, DIAGNOSIS'

    for vals in header_values[:-1]:
        headers_without_types += (', ' + 'Entrez_id_' + str(vals))
        headers_with_types += (', ' + 'Entrez_id_' + str(vals) + ' double')
    headers_without_types += ('Entrez_id_' + str(header_values[-1]))
    headers_with_types += (', Entrez_id_' + str(header_values[-1]) + ' double')
    return headers_with_types, headers_without_types


def load_data_file(file):
    rosmap =  pd.read_csv(file)
    rosmap = rosmap.replace(np.nan, -1.0)
    return rosmap


def create_table(headers, keyspace_name, table_name):
    cluster = Cluster()
    session = cluster.connect(keyspace_name)
    session.execute("""
                    CREATE TABLE IF NOT EXISTS {} ({});
                    """.format(table_name, headers))


def get_insert_db_line(row):
    import pdb;
    pdb.set_trace()
    line_to_insert = []
    line_to_insert.append(row[0])
    for item in enumerate(row[1:]):
        line_to_insert.append(item[1])
    pdb.set_trace()
    return line_to_insert
    #line_to_insert = str(row[0]) + ', '
    #for item in enumerate(row[1:-1]):
    #    line_to_insert += str(item[1]) + ', '
    #line_to_insert += str(row[-1])
    #return line_to_insert


def populate_table(headers_without_types, keyspace_name, rosmap, table_name):
    cluster = Cluster()
    session = cluster.connect(keyspace_name)

    import pdb; pdb.set_trace()
    for entry in enumerate(rosmap):
        insert_line = get_insert_db_line(rosmap.loc[entry[0]])
        #pdb.set_trace()
        print(entry[0])
        session.execute("""
                        INSERT INTO {}({})
                        VALUES ({})
                        """.format(table_name,
                                   headers_without_types,
                                   insert_line)
                        )


#---- Main --------------------------------------------------------------------

file = '../ROSMAP_RNASeq_entrez.csv'
keyspace_name = 'rosmap_rna'
table_name = 'patient_diagnosis'
rosmap = load_data_file(file)
headers_with_types, headers_without_types = get_headers(rosmap)
create_cql_keyspace(keyspace_name)
create_table(headers_with_types, keyspace_name, table_name)
populate_table(headers_without_types, keyspace_name, rosmap, table_name)


#cleaned_rosmap = []

#with open('../ROSMAP_RNASeq_entrez.csv', 'r') as infile:
#    data = csv.reader(infile, delimiter=',')
#    for line in data:
#        clean_line = ''
#        for word in line[:-1]:
#            clean_line += (word + ', ')
#        clean_line += line[-1]
#        cleaned_rosmap.append(clean_line)

#session = cluster.connect(table_name)
#session.execute("""
#                CREATE TABLE IF NOT EXISTS patient_diagnosis( {} );
#                """ .format(headers_with_types))
#
##import pdb; pdb.set_trace()
#
#for line in cleaned_rosmap[1:]:
#    session.execute("""
#                    INSERT INTO patient_diagnosis({})
#                    VALUES ({})
#                    """.format(headers_without_types, line))






