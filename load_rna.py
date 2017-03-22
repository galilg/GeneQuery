
#---- Imports -----------------------------------------------------------------

from cassandra.cluster import Cluster

import Rosmap as rna

def mean_and_std(self, category, gene_id):
    column_name = 'entrez_id_' + str(gene_id)
    mean_and_std = self.get_mean_and_std(category, column_name)
    return mean_and_std

import pdb; pdb.set_trace()
rosmap = rna.Rosmap()

rosmap_data = rosmap.load_data_file(rosmap.file_location)
headers_with_types, headers_without_types = rosmap.get_headers(
                                                            rosmap_data
                                                               )
rosmap.create_cql_keyspace()
rosmap.create_table(headers_with_types,
                    rosmap.keyspace_name,
                    rosmap.table_name)
rosmap.populate_table(headers_without_types,
                      rosmap.keyspace_name,
                      rosmap_data,
                      rosmap.table_name)

m_std = mean_and_std('NCI', 3)
print('Mean: {} , Std: {} ' .format(m_std[0], m_std[0]))

