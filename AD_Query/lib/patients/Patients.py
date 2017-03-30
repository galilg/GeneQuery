#---- Imports -----------------------------------------------------------------

import csv
import os
import pymysql

from pymysql import connect, err, sys, cursors


#---- Public Classes ----------------------------------------------------------

class Patients(object):
    def __init__(self, csv_file=None):
        self.__db_exists = False
        self.__table_exists = False
        self.__patients_db = None
        if csv_file is None:
            self.__csv_file = \
              '/Users/galil/src/ad_gene_query/input_data/patients.csv'
        else:
            self.__csv_file = csv_file

    def create_database(self):
        if self.__db_exists:
            return
        self.__patients_db = connect(host='localhost',
                                     user='',
                                     passwd='',
                                     db = '')
        cursor = self.__patients_db.cursor()
        sql = """
              CREATE DATABASE IF NOT EXISTS AD_db
              """
        cursor.execute(sql)


    def create_table(self):
        if self.__table_exists:
            return
        self.__patients_db = connect(host='localhost',
                                     user='',
                                     passwd='',
                                     db='AD_db')

        cursor = self.__patients_db.cursor()

        sql = """
              CREATE TABLE IF NOT EXISTS patients(
              patient_id VARCHAR(11) PRIMARY KEY,
              age int(11) DEFAULT NULL,
              gender VARCHAR(2) DEFAULT NULL,
              education VARCHAR(10) DEFAULT NULL
              ) ENGINE=MyISAM DEFAULT CHARSET=latin1
              """
        cursor.execute(sql)


    def load_csv_into_database(self):
        #self.__patients_db = connect(host='localhost',
        #                             user='',
        #                             passwd='',
        #                             db='AD_db')

        cursor = self.__patients_db.cursor()
        csv_data = csv.reader(open(self.__csv_file))
        next(csv_data, None)
        #import pdb; pdb.set_trace()
        for row in csv_data:
            sql = ("""
                   INSERT INTO `patients`(`patient_id`, `age`, `gender`, `education`) VALUES (%s, %s, %s, %s) """)#.format(row[0], row[1], row[2], row[3])

            cursor.execute(sql, row)


    def get_patient_info(self, id):
        self.__patients_db = connect(host='localhost',
                                     user='',
                                     passwd='',
                                     db='AD_db')
        cursor = self.__patients_db.cursor()
        sql = ("""SELECT p.age, p.gender, p.education from patients as p
                          WHERE patient_id = %s
                       """)
        cursor.execute(sql, id)
        result = cursor.fetchone()

        return result
