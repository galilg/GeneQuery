#!/usr/bin/python3 /usr/bin/env

import EntrezUniprotMap

entrez_file = '/Users/galil/src/ad_gene_query/input_data/e2u_map'
map = EntrezUniprotMap.EntrezUniprotMap(entrez_file)

test = map.get_values(140690)
print("values for 140690 are: ", test)
