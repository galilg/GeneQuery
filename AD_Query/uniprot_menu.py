#---- Imports -----------------------------------------------------------------

from lib.uniprot_genes.UniprotQuery import UniprotQuery

import lib.uniprot_genes.EntrezUniprotMap  as e2u_map
import sys

#---- Functions ---------------------------------------------------------------
def display_menu():
    print(
"""
1 - Load uniprot xml file into the databsse
2 - Get gene info with entrez id
q - Return to main menu
""")
    command = input("Please select: ")
    return command


def call_uniprot_gene_stats():
    command = True
    while(command):
        command = display_menu()
        if (command == '1'):
            print("Enter the filepath where the UNIPROT file is located? \n"
                  "Choose N to use the default filepath (not recommended.")
            has_file = input("Y/N: ")
            if (has_file.lower() == 'y'):
                entrez_file = input('File path: ')
            else:
                entrez_file = None
            map = e2u_map.EntrezUniprotMap(entrez_file)
            map.load_csv_to_redis()
            u_query = UniprotQuery()
            import pdb; pdb.set_trace()
            u_query.load_uniprot_xml('/Users/galil/src/uniprot-human.xml')
            # Add here loading the actual XML into the database

        elif (command == '2'):
            subcommand = True
            while(subcommand):
                u_query = UniprotQuery()
                map = e2u_map.EntrezUniprotMap()
                subcommand = input("Enter entrez id (q to quit): ")
                import pdb; pdb.set_trace()
                if (subcommand == 'q'):
                    subcommand = False
                #print("Values: ", map.get_values(subcommand))
                uniprot_ids = map.get_values(subcommand)
                for gene in uniprot_ids:
                    print(u_query.get_gene_data(gene))


        elif (command == 'q'):
            command = False
