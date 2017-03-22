#!/usr/bin/env

#---- Imports -----------------------------------------------------------------
import RNA_data as rd

#from cassandra.cluster import Cluster
#
#import cassandra.query
#import csv
#import pandas as pd
#import math
#import timeit
#import Rosmap as rna
#
#---- Main --------------------------------------------------------------------
rna_data = rd.RNA_data()
entrez_9 = rna_data.mean_and_std('NCI', 1)
print('''The mean of entrez_9 is : {}\n
       The std of entrez_9 is : {} ''' .format(entrez_9[0], entrez_9[1]))
#
#rosmap = rna.Rosmap()
#std_nci = rosmap.get_std('NCI', 'entrez_id_3')
#std_mci = rosmap.get_std('MCI', 'entrez_id_3')
#std_ad = rosmap.get_std('AD', 'entrez_id_3')
#std_others = rosmap.get_std('OTHERS', 'entrez_id_3')
#print("MEAN: {}\nSTD NCI: {}".format(std_nci[0], std_nci[1]))
#print("MEAN: {}\nSTD MCI: {}".format(std_mci[0], std_mci[1]))
#print("MEAN: {}\nSTD AD: {}".format(std_ad[0], std_ad[1]))
#print("MEAN: {}\nSTD OTHERS: {}".format(std_others[0], std_others[1]))
##average = rosmap.get_mean('diagnosis')
##print(average[0].system_avg_diagnosis)
##print(average[0].col)
##for x in average:
##    print(x)
#
##rosmap.fix_grace_seconds()
#patient_ids = rosmap.get_column('patient_id')
#diagnosis = rosmap.get_column('diagnosis')

#for entry in diagnosis:
#    print(entry)

#for entry in patient_ids:
#    print(entry.patient_id)
