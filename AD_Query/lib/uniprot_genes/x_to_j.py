#!/usr/bin/python3 /usr/bin/env

#import xml.etree.ElementTree as ET
#import json, xmljson
#from lxml.etree import fromstring, tostring
#
#tree = ET.parse('../../input_data/uniprot-human.xml')
#root = tree.getroot()
#data = fromstring(root)
##data =
#print(json.dumps(xmljson.badgerfish.data(data)))


from lxml import objectify
import pandas as pd

path = '../../input_data/test_data.xml'
#xml = objectify.parse(open(path))
#
#root = xml.getroot()
#root.getchildren()[0].getchildren()
#df = pd.DataFrame(columns=('id', 'name'))
#
#for i in range(0,400):
#    import pdb; pdb.set_trace()
#    obj = root.getchildren()[i].getchildren()
#    row = dict(zip(['id', 'name'], [obj[0].text, obj[1].text]))
#    print(row)
#    row_s = pd.Series(row)
#    row_s.name = i
#    df = df.append(row_s)
#
#print(df)


import json
import xmltodict
import pprint

path = '../../input_data/test2.xml'

def handle_entry(_, entry):
    entry = json.dumps(entry, indent=4)
    print(entry)
    return True

def convert(xml_file, xml_attribs=True):

    with open(xml_file, "rb") as f: # notice the "rb" mode
        xmltodict.parse(f, xml_attribs=xml_attribs, item_depth=2, item_callback=handle_entry)

    #return json.dumps(d, indent=4)



convert(path)


#def convert(xml_file, xml_attribs=True):
#
#    with open(xml_file, "rb") as f: # notice the "rb" mode
#        d = xmltodict.parse(f, xml_attribs=xml_attribs, )
#
#    return json.dumps(d, indent=4)
#
#
#
#json_format = convert(path)
#
#print(json_format)
