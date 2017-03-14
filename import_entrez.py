#!/usr/bin/env

import re

def is_begining_of_entrez_id(line):
    return bool(re.compile(r'[0-9]').match(line[0][:5]))


data = []
with open('../Entrez_copy', 'r') as f:
    for line in f:
        data.append(line.split("HUMAN"))

header = ("entrez_id, uniprot_id, gene_name, description")

print("THE FREAKIN header: ", header)

data = data[1:]
new_data =[]
for line in data:
    if (is_begining_of_entrez_id(line)):
        ids = line[0].split(" ")
        gene_name = line[1].split('(')
        ids[0] = ids[0].rstrip()
        ids[1] = ids[-1].strip() + 'HUMAN'
        gene_name[0] = gene_name[0].lstrip()
        gene_name[1] = gene_name[1][:-2]
        new_line = [ids[0], ids[1], gene_name[1], gene_name[0]]
        new_data.append(new_line)

print(new_data)
with open('Entrez_id.csv', 'w') as outfile:
    outfile.write(header)
    outfile.write('\n')
    for line in new_data:
        for word in line:
            if word == line[-1]:
                outfile.write(word)
            else:
                outfile.write(word + ", ")
        outfile.write('\n')

