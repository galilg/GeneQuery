#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

from pymongo import MongoClient

import json
import pymongo
import xmltodict


#---- Public Classes ----------------------------------------------------------

class UniprotQuery(object):

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.uniprot
        self.entries = self.db.genes


    def get_gene_data(self, uniprot_id):
        return self.entries.findOne({'name': uniprot_id})

    def load_entry_to_mongo(self, _, entry):
        item = json.dumps(entry, indent=4)
        json_item = json.loads(entry)
        result = self.entries.insert_one(json_item)
        print('One item: {}' .format(result.inserted_id))
        return True

    def load_uniprot_xml(self, xml_file, xml_attribs=True):
        with open(xml_file, 'rb') as f:
            xmltodict.parse(f, xml_attribs=xml_attribs,
                            item_depth=2,
                            item_callback=self.load_entry_to_mongo)
