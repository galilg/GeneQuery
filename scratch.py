
#!/usr/bin/env

from cassandra.cluster import Cluster

import csv
import pandas as pd
import math

rosmap =  pd.read_csv('../ROSMAP_RNASeq_entrez.csv')

diagnosis = rosmap['DIAGNOSIS']
for val in diagnosis:
    if math.isnan(val):
        val = -1
        print(val)

