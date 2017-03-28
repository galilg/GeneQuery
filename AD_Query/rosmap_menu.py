#---- Imports -----------------------------------------------------------------

import lib.rosmap.RNA_data as rna
import sys

#---- Funcions ----------------------------------------------------------------
def display_menu():
    print(
"""
1 - Load csv file into the database
2 - Get mean value and standard deviation of a gene in database
3 - Return to main menu
""")
    command = input("Please select: ")
    return command

def call_rosmap_gene_stats():
    command = True
    rna_data = rna.RNA_data()
    while (command):

        command = display_menu()
        if (command == '1'):
            print("Enter the filepath where the ROSMAP file is located? \n"
                  "Choose N to use the default filepath (notrecommended).")
            has_file = input("Y/N: ")
            if (has_file.lower() == 'y'):
                file = input("File name: ")
            else:
                file = None
            print("Loading RNA data into database ...")
            rna_data.load_rna_data(file)

        elif (command == '2'):
            entrez_id = 's'
            while not(entrez_id.isdigit()):
                entrez_id = input( \
                    "Enter entrez id for the gene you are looking for: ")
            research_group = input( \
                    "Enter the research group: NCI|MCI|AD|OTHER: ")
            research_group = research_group.upper()
            if not(research_group == 'NCI' or
                   research_group == 'MCI' or
                   research_group == 'AD'):
                research_group = 'other'
            else:
                research_group = research_group
            m_and_s = rna_data.mean_and_std(research_group, entrez_id)
            if m_and_s is False:
                print("That entrez if does not exist.")
            else:
                print("The mean for entrez id {} is: {}"
                                .format(entrez_id, m_and_s[0]))
                print("The standard deviation for entrez id {} is: {}"
                                .format(entrez_id, m_and_s[1]))
        elif(command == '3'):
            command = False
