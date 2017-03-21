#!/usr/bin/env

#---- Imports -----------------------------------------------------------------

import Rosmap as rna

#---- Main --------------------------------------------------------------------

rosmap = rna.Rosmap()

rosmap_data = rosmap.load_data_file(rosmap.file_location)
headers_with_types, headers_without_types = rosmap.get_headers(rosmap_data)
rosmap.create_cql_keyspace(rosmap.keyspace_name)
rosmap.create_table(headers_with_types,
                    rosmap.keyspace_name,
                    rosmap.table_name)
rosmap.populate_table(headers_without_types,
                      rosmap.keyspace_name,
                      rosmap_data,
                      rosmap.table_name)
