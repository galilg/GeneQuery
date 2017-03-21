#!/usr/bin/env

#---- Imports -----------------------------------------------------------------

from cassandra.cluster import Cluster

import cassandra.query
import csv
import pandas as pd
import math
import timeit
import Rosmap as rna

#---- Main --------------------------------------------------------------------

rosmap = rna.Rosmap()
rosmap.get_column_std('diagnosis')
#rosmap.calc_mean('diagnosis')
#average = rosmap.get_mean('diagnosis')
#print(average[0].system_avg_diagnosis)
#print(average[0].col)
#for x in average:
#    print(x)

#rosmap.fix_grace_seconds()
#patient_ids = rosmap.get_column('patient_id')
#diagnosis = rosmap.get_column('diagnosis')

#for entry in diagnosis:
#    print(entry)

#for entry in patient_ids:
#    print(entry.patient_id)
