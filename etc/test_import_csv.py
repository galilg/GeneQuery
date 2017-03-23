from cassandra.cluster import Cluster
import pandas as pd
import csv

#data = pd.read_csv('test.csv')
#print(data)

clean_data = []
#with open('test.csv', 'r') as csvfile:
#    data = csv.reader(csvfile, delimiter=',')
#    for line in data:
#        clean_line = ''
#        for word in line[:-1]:
#            clean_line += (word + ', ')
#        clean_line += ( (line[-1]))
#        clean_data.append(clean_line)


num_with_types = 'name text, num1 double primary key, num2 double, num3 double'
num_list = 'name, num1, num2, num3'

cluster = Cluster()
session = cluster.connect('test_space')
session.execute("""
                CREATE TABLE IF NOT EXISTS test_table({});
                """.format(num_with_types)
                )
#import pdb; pdb.set_trace()

vals = "'X593kdIJJ', 3.4, 4.7, 5.2"

    #print("The line: ", line)
print("""
       INSERT INTO {}({})
       VALUES ({})
       """.format('test_table', num_list, vals)
       )
session.execute("""
                 INSERT INTO test_table({})
                 VALUES({})
                 """.format(num_list, vals)
                 )

