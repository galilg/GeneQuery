from cassandra.cluster import Cluster
import pandas as pd
import csv

#data = pd.read_csv('test.csv')
#print(data)

clean_data = []
with open('test.csv', 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for line in data:
        clean_line = ''
        for word in line[:-1]:
            clean_line += (word + ', ')
        clean_line += ( (line[-1]))
        clean_data.append(clean_line)

cluster = Cluster()
session = cluster.connect('test_space')
#session.execute("""
#                CREATE TABLE IF NOT EXISTS test_table
import pdb; pdb.set_trace()
for line in clean_data[1:]:
    #print("The line: ", line)
    session.execute("""
                    INSERT INTO test_table(num1, num2, num3)
                    VALUES({})
                    """.format(line))
