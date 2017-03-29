#---- Imports -----------------------------------------------------------------

import re

#---- Functions ---------------------------------------------------------------

def convert_data_to_csv_format(data):
    csv_data =[]
    for line in data:
        if (is_begining_of_entrez_id(line)):
            ids = line[0].split(" ")
            gene_name = line[1].split('(')
            ids[0] = ids[0].rstrip()
            ids[1] = ids[-1].strip() + 'HUMAN'
            gene_name[0] = gene_name[0].lstrip()
            gene_name[0] = re.sub(r',', '', gene_name[0])
            gene_name[1] = gene_name[1][:-2]
            #new_line = [ids[0],ids[1],gene_name[1],gene_name[0]]
            new_line = [ids[0],ids[1]]
            csv_data.append(new_line)
    return csv_data


def is_begining_of_entrez_id(line):
    return bool(re.compile(r'[0-9]').match(line[0][0]))


def open_entrez_id_file(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(line.split("HUMAN"))

    return data

