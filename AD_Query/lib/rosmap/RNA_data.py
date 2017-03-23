#---- Imports -----------------------------------------------------------------

from cassandra.cluster import Cluster

from . import Rosmap as rna

#---- Classes -----------------------------------------------------------------

class RNA_data(object):
    def __init__(self):
        self.rosmap = rna.Rosmap()
        self.file_location = self.rosmap.file_location


    def load_rna_data(self, file=None):
        if file is None:
            rosmap_data = self.rosmap.load_data_file(self.file_location)
        else:
            rosmap_data = self.rosmap.load_data_file(file)

        headers_with_types, headers_without_types = \
                                    self.rosmap.get_headers(rosmap_data)
        self.rosmap.create_cql_keyspace()
        self.rosmap.create_table(headers_with_types,
                            self.rosmap.keyspace_name,
                            self.rosmap.table_name)
        self.rosmap.populate_table(headers_without_types,
                              self.rosmap.keyspace_name,
                              rosmap_data,
                              self.rosmap.table_name)


    def mean_and_std(self, category, gene_id):
        #import pdb; pdb.set_trace()
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect('rosmap_rna')
        column_name = 'entrez_id_' + str(gene_id)
        mean_and_std = self.rosmap.get_mean_and_std(category, column_name)
        if mean_and_std is False:
            return False
        return mean_and_std
