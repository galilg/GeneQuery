#---- Imports -----------------------------------------------------------------

from cassandra.cluster import Cluster

import Rosmap as rna

#---- Classes -----------------------------------------------------------------

class RNA_data(object):
    def __init__(self):
        #import pdb; pdb.set_trace()
        self.rosmap = rna.Rosmap()

        self.rosmap_data = self.rosmap.load_data_file(self.rosmap.file_location)
        headers_with_types, headers_without_types = \
                                    self.rosmap.get_headers(self.rosmap_data)
        self.rosmap.create_cql_keyspace()
        self.rosmap.create_table(headers_with_types,
                            self.rosmap.keyspace_name,
                            self.rosmap.table_name)
        self.rosmap.populate_table(headers_without_types,
                              self.rosmap.keyspace_name,
                              self.rosmap_data,
                              self.rosmap.table_name)


    def mean_and_std(self, category, gene_id):
        #import pdb; pdb.set_trace()
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect('rosmap_rna')
        column_name = 'entrez_id_' + str(gene_id)
        mean_and_std = self.rosmap.get_mean_and_std(category, column_name)
        return mean_and_std
