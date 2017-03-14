#!/usr/bin/env

import re

data = []
with open('../Entrez_id_uniprot_mapping', 'r') as f:
    for line in f:
        data.append(line.split("HUMAN"))

header = ("entrez_id, uniprot_id, gene_name, description")

print("THE FREAKIN header: ", header)

data = data[1:]
new_data =[]
for line in data:
    ids = line[0].split(" ")
    print("ids: ", ids)
    gene_name = line[1].split('(')
    ids[0] = ids[0].rstrip()
    #print("Id 1: ", ids[1])
    ids[1] = ids[-1].strip() + 'HUMAN'
    #print("Id 2: ", ids[1])
    gene_name[0] = gene_name[0].lstrip()
    gene_name[1] = gene_name[1][:-2]
    new_line = [ids[0], ids[1], gene_name[1], gene_name[0]]
    print("The new line: ", new_line)
    new_data.append(new_line)

print(new_data)
with open('../Entrez_id.csv', 'w') as outfile:
    for line in new_data:
        for word in line:
            if word == line[-1]:
                outfile.write(word)
            else:
                outfile.write(word + ", ")
        outfile.write('\n')

