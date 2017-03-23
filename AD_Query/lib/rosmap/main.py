#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

from cassandra.cluster import Cluster

import RNA_data as rna


#---- Main --------------------------------------------------------------------

# Create and load the table with the csv file
#import pdb; pdb.set_trace()
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('rosmap_rna')

rna_data = rna.RNA_data()
rna_data.load_rna_data()
###############################################################################
# Find the mean and standard deviation of an entrez id among patients:        #
#                                                                             #
#   rna_data.mean_and_std(<'NCI'|'MCI'|'AD'|'OTHER'>, <Entrez ID>)            #
###############################################################################


# Sample queries of gene mean and standard deviation:

entrez_1 = rna_data.mean_and_std('NCI', 1)
print("Mean for NCI patients on Entrez id 9:{}\nSTD for same:{}".format(
                                                entrez_1[0], entrez_1[1])
                                                )

entrez_3 = rna_data.mean_and_std('AD', 3)
print("Mean for AD patients on Entrez id 3:{}\nSTD for same:{}".format(
                                                entrez_3[0], entrez_3[1])
                                                )
