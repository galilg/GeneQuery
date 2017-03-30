#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

import redis
from . import import_entrez as e2u
#---- Public Classes ----------------------------------------------------------

class EntrezUniprotMap(object):

    def __init__(self, entrez_file=None):
        if entrez_file is None:
            self.__entrez_file = '/Users/galil/src/ad_gene_query/input_data/e2u_map'
        else:
            self.__entrez_file = entrez_file
        self.__e2u_map = redis.StrictRedis()
        self.__csv_data = []


    def __add_item_to_db(self, pair):
        self.__e2u_map.lpush(pair[0], pair[1])


    def add_key_value(self, key, value):
        self.__e2u_map.lpush(key, value)


    def __convert_input_to_csv(self):
        data = e2u.open_entrez_id_file(self.__entrez_file)
        self.__csv_data = e2u.convert_data_to_csv_format(data)


    def __decode_bytes(self, byte):
        return byte.decode('utf-8')


    def get_values(self, key):
         byte_list =  self.__e2u_map.lrange(key, 0, -1)
         uniprot_id_list = []
         for id in byte_list:
            uniprot_id_list.append(self.__decode_bytes(id))
         return uniprot_id_list


    def load_csv_to_redis(self):
        self.__convert_input_to_csv()
        for line in self.__csv_data:
            self.__add_item_to_db(line)
