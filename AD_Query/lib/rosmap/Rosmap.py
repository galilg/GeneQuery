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
                 file_location = '/Users/galil/src/ad_gene_query/input_data/ROSMAP_RNASeq_entrez.csv',
                 keyspace_name = "rosmap_rna",
                 table_name = 'patient_diagnosis'
                 ):
        self.file_location = file_location
        self.keyspace_name = keyspace_name
        self.table_name = table_name

    def create_cql_keyspace(self):
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect()
        session.execute("""
                              CREATE KEYSPACE IF NOT EXISTS {}
                              WITH replication = {{ 'class': 'SimpleStrategy',
                                                   'replication_factor': 12}};
                              """ .format(self.keyspace_name))


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


    def __get_column_df(self, column, lower_bound, upper_bound):
        session = self.__start_session()
        session.row_factory = self.pandas_factory
        session.default_fetch_size = 10000000
        try:
            rows = session.execute("""
                               SELECT {}
                               FROM {}
                               WHERE diagnosis >= {}
                               and diagnosis < {}
                               ALLOW FILTERING
                               """.format(column,
                                          self.table_name,
                                          lower_bound,
                                          upper_bound)
                               )
            df = rows._current_rows
            return df
        except Exception as e:
            #import pdb; pdb.set_trace()
            print("That is not a valid entrez id.")
            excepName =type(e).__name__

    def get_mean_and_std(self, category, column):
        #import pdb; pdb.set_trace()
        session = self.__start_session()
        group = category.upper()
        if (group == 'NCI'):
            lower_bound, upper_bound = 0.0, 2.0
        elif (group == 'MCI'):
            lower_bound, upper_bound = 2.0, 4.0
        elif (group == 'AD'):
            lower_bound, upper_bound = 4.0, 6.0
        else:
            lower_bound, upper_bound = 6.0, 10.0

        df = self.__get_column_df(column, lower_bound, upper_bound)
        if df is None:
            return False
        return [df.values.mean(), df.values.std(ddof=1)]


    def __get_insert_db_line(self, row):
        line_to_insert = []
        line_to_insert.append(row[0])
        for item in enumerate(row[1:]):
            line_to_insert.append(item[1])
        return line_to_insert


    def load_data_file(self, file):
        rosmap =  pd.read_csv(file)
        rosmap = rosmap.replace(np.nan, 0.0) # Set all NaN values to -1.0
        return rosmap                        # RNA values are all positive


    def pandas_factory(self, colnames, rows):
        return pd.DataFrame(rows, columns=colnames)


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
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect(self.keyspace_name)
        return session
