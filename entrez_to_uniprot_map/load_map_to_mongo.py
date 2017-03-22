#!/usr/bin/python3 /usr/bin/end

#---- Imports -----------------------------------------------------------------

from pymongo import MongoClient

import csv
import pprint
import pymongo

#---- Initialize Database -----------------------------------------------------

client = MongoClient()
db = client.AD_db
id_map = db.entrez_uniprot
id_map.remove()
#---- Load CSV map ------------------------------------------------------------

csv_infile = 'entrez_id_to_uniprot_id_only.csv'
#csv_infile = 'test.csv'
reader = csv.reader(open(csv_infile, 'r'))

for row in reader:
    item = id_map.find_one({'entrez_id': row[0]})
    if (item != None):
        # Push the new uniprot to the uniprot list
        record = item
        id = record['_id']
        #print(id)
        id_map.update(
            { 'entrez_id': row[0] },
            { '$push': { 'uniprot_ids': row[1] } }
        )
    else:
        # Insert new element
        id_map.insert_one({'entrez_id': row[0], 'uniprot_ids': [row[1]]})

pprint.pprint(id_map.find_one({'entrez_id': '23658'}))
