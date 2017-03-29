#!/usr/bin/python3 /usr/bin/env

import pymysql.cursors
from pymysql import connect, err, sys, cursors

def create_database():
    # create the db
    pass

def create_table(database):
    # create table here
    pass

#---- Main --------------------------------------------------------


# create_database

db1=pymysql.connect(host='localhost', user='', passwd='', db='genes')
cursor=db1.cursor()
#import pdb; pdb.set_trace()
sql="""CREATE DATABASE IF NOT EXISTS genes"""

cursor.execute(sql)
#cursor=conn.cursor(cursors.DictCursor
#cursor.execute('''CREATE TABLE IF NOT EXISTS `patients`
#        (
#         `patient_id` VARCHAR(11) COLLATE utf8_bin NOT NULL,
#         `age` int(11)  NOT NULL,
#         `gender` VARCHAR(1) COLLATE utf8_bin  NOT NULL,
#         `education` VARCHAR(3) COLLATE utf8_bin  NOT NULL
#          PRIMARY KEY (`patient_id`)
#)Engine = InnoDB  DEFAULT CHARSER=utf8 COLLATE=utf8_bin''')

sql='''
      CREATE TABLE IF NOT EXISTS patients_data (
      patient_id VARCHAR(11) DEFAULT NULL,
      age int(11) DEFAULT NULL,
      gender VARCHAR(2) DEFAULT NULL,
      education VARCHAR(10) DEFAULT NULL
      ) ENGINE=MyISAM DEFAULT CHARSET=latin1
         '''
cursor.execute(sql)
import csv
#with open('/home/galil/src/genes/gene-env/patients.csv', 'r') as csv_file:
#    csv_data = csv.reader(csv_file)
#    next(csv_data)
csv_data=csv.reader(open('/Users/galil/src/ad_gene_query/AD_Query/input_data/patients.csv'))
next(csv_data, None)
for row in csv_data:
    sql=""" INSERT INTO patients_data (patient_id, age, gender, education) VALUES(%s, %s, %s, %s)"""
    cursor.execute(sql, row)
