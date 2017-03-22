#!/usr/bin/env

#---- Imports -----------------------------------------------------------------

from cassandra.cluster import Cluster

import Rosmap as rna

#---- Classes -----------------------------------------------------------------

class RNA_data(object):
    def __init__(self):
        self.rosmap = rna.Rosmap()

        rosmap_data = self.rosmap.load_data_file(rosmap.file_location)
        headers_with_types, headers_without_types = rosmap.get_headers(
                                                                    rosmap_data
                                                                       )
        self.rosmap.create_cql_keyspace(rosmap.keyspace_name)
        self.rosmap.create_table(headers_with_types,
                            rosmap.keyspace_name,
                            rosmap.table_name)
        self.rosmap.populate_table(headers_without_types,
                              rosmap.keyspace_name,
                              rosmap_data,
                              rosmap.table_name)


    def mean_and_std(self, category, gene_id):
        cluster = Cluster()
        session = cluster.connect(self.rosmap.keyspace_name)
        column_name = 'entrez_id_' + str(gene_id)
        mean_and_std = self.rosmap.get_mean_and_std(category,
        return mean_and_std
