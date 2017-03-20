#!/usr/bin/env

import xml.etree.ElementTree as ET
from lxml import etree
import pandas as pd

xml_data = '../uniprot-human.xml'

def xml2df(xml_data):
    tree = ET.parse(xml_data)
    root = tree.getroot()
    all_records = []
    headers = []
    for child in root[:20]:
        print(child.tag)
    #for i, child in enumerate(root):
    #    record = []
    #    for subchild in child:
    #        record.append(subchild.text)
    #        if subchild.tag not in headers:
    #            headers.append(subchild.tag)
    #    all_records.append(record)
    #return pd.DataFrame(all_records, columns=headers)
    #return tree


#df = xml2df(xml_data)
#something =
xml2df(xml_data)

#print(df.head(n=10))
