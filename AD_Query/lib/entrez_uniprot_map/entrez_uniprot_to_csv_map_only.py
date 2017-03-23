#!/usr/bin/env

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


def save_to_csv_file(cleaned_data):
    with open('../entrez_id_to_uniprot_id_only.csv', 'w') as outfile:
        #header = "entrez_id,uniprot_id,gene_name,description"
        header = "entrez_id,uniprot_id"
        outfile.write(header)
        outfile.write('\n')
        for line in cleaned_data:
            for word in line:
                if word == line[-1]:
                    outfile.write(word)
                else:
                    outfile.write(word + ",")
            outfile.write('\n')


#---- Main --------------------------------------------------------------------

file_path = '../entrez_id_uniprot_mapping'
data = open_entrez_id_file(file_path)
csv_data = convert_data_to_csv_format(data)
save_to_csv_file(csv_data)
