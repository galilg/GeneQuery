#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

from EntrezUniprotMap import EntrezUniprotMap

#---- Main --------------------------------------------------------------------

entrez_file = '/Users/galil/src/ad_gene_query/entrez_to_uniprot_map/entrez_id_uniprot_mapping'

map = EntrezUniprotMap(entrez_file)
#map.convert_input_to_csv()
#map.load_csv_to_redis()
test = map.get_values(140690)
print("The values for 140690: ", test)
