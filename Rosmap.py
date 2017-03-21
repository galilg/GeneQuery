#!/usr/bin/env

#---- Imports -----------------------------------------------------------------

from cassandra.cluster import Cluster
from cassandra.query import tuple_factory

import csv
import math
import numpy as np
import pandas as pd


#---- Public Classes ----------------------------------------------------------

class Rosmap(object):
    '''
    Imports the ROSMAP_RNA_Seq.csv file
    and is able to manipulate it and query it.
    '''

    def __init__(self,
                 file_location = '../ROSMAP_RNASeq_entrez.csv',
                 keyspace_name = "rosmap_rna",
                 table_name = 'patient_diagnosis'
                 ):
        self.file_location = file_location
        self.keyspace_name = keyspace_name
        self.table_name = table_name


    def create_cql_keyspace(self, keyspace_name):
        session = self.__start_session()
        key = session.execute("""
                              CREATE KEYSPACE IF NOT EXISTS {}
                              WITH replication = {{ 'class': 'SimpleStrategy',
                                                   'replication_factor': 5}};
                              """ .format(keyspace_name))


    def create_table(self, headers, keyspace_name, table_name):
        session = self.__start_session()
        headers = ', '.join(headers)
        session.execute("""
                        CREATE TABLE IF NOT EXISTS {} ({});
                        """.format(table_name, headers))


    def get_headers(self, rosmap):
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
        return (headers_with_types, headers_without_types)


    def get_column(self, column):
        session = self.__start_session()
        num = session.execute("""
                              SELECT {} FROM {}
                              """.format(column, self.table_name))
        return num


    def __get_insert_db_line(self, row):
        line_to_insert = []
        line_to_insert.append(row[0])
        for item in enumerate(row[1:]):
            line_to_insert.append(item[1])
        return line_to_insert


    def get_mean(self, column):
        session = self.__start_session()
        vals = session.execute("""
                              SELECT {} FROM {}
                              """.format(column, self.table_name)
                              )
        val_sum = 0.0
        count = 0
        for num in vals:
            if(getattr(num, column, None) >= 0.0):
                val_sum += getattr(num, column, None)
                count += 1
        if(count > 0):
            return (val_sum/(float(count)))
        return 0

    def load_data_file(self, file):
        rosmap =  pd.read_csv(file)
        rosmap = rosmap.replace(np.nan, 0.0)
        return rosmap


    def populate_table(self,
                       headers_without_types,
                       keyspace_name,
                       rosmap,
                       table_name):
        session = self.__start_session()
        headers_without_types = ', '.join(headers_without_types)
        #import pdb; pdb.set_trace()
        for entry in range(0, len(rosmap.index)):
            insert_line = self.__get_insert_db_line(rosmap.loc[entry])
            line = ', '.join(str(v) for v in insert_line)
            patient_id = "'"+line[0:11] +"'"
            line = line[11:]
            data_to_insert = patient_id + line
            session.execute("""
                            INSERT INTO {}({})
                            VALUES ({})
                            """.format(table_name,
                                       headers_without_types,
                                       data_to_insert)
                            )


    def __start_session(self):
        cluster = Cluster()
        session = cluster.connect(self.keyspace_name)
        return session


    def fix_grace_seconds(self):
        session = self.__start_session()
        session.execute("""
                        ALTER TABLE {}
                        WITH GC_GRACE_SECONDS = 0
                        """.format(self.table_name))





