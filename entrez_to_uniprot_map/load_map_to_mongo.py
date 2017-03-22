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
last_entrez = 0
last_id = 0
for row in reader:
    #item = id_map.find_one({'entrez_id': row[0]})
    #if (item != None):
    #if(item != None and item['entrez_id'] == last_entrez):
    if(row[0] == last_entrez):
        # Push the new uniprot to the uniprot list

        id_map.update(
            { 'entrez_id': row[0] },
            { '$push': { 'uniprot_ids': row[1] } }
        )
        last_entrez = row[0]
    else:
        # Insert new element
        last_id = id_map.insert_one({'entrez_id': row[0],
                                     'uniprot_ids': [row[1]]}).inserted_id
        last_entrez = row[0]


pprint.pprint(id_map.find_one({'entrez_id': '23658'}))
