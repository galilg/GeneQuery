#!/usr/bin/python3 /usr/bin/env

from ...lib.uniprot_genes.EntrezUniprotMap import EntrezUniprotMap

entrez_file = '/Users/galil/src/ad_gene_query/AD_Query/input_data/e2u_map'
map = EntrezUniprotMap(entrez_file)

test = map.get_values(140690)
print("values for 140690 are: ", test)
