#---- Imports -----------------------------------------------------------------

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
            # Add here loading the actual XML into the database

        elif (command == '2'):
            pass

        elif (command == 'q'):
            command = False
