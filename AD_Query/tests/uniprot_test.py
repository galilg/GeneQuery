#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

import lib.uniprot_genes.UniprotQuery.UniprotQuery


#---- Main --------------------------------------------------------------------

test_xml = '../../input_data/test2.xml'
test_mongo = UniprotQuery()
test_mongo.load_uniprot_xml(test_xml)
