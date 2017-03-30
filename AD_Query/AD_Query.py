#!/usr/bin/python /usr/bin/env

#---- Imports -----------------------------------------------------------------

from main_menu import display_menu


import patients_menu
import rosmap_menu
import sys
import uniprot_menu


#---- Main --------------------------------------------------------------------
#rna_data = rna.RNA_data()
#biogrid = bio.Biogrid()

#import pdb; pdb.set_trace()
command = True
while(command):
    command = display_menu()
    if (command == '1'):
        patients_menu.call_patients_info()
        pass
    elif(command == '2'):
        uniprot_menu.call_uniprot_gene_stats()

    elif(command == '3'):
        # Call interacting genes
        pass
    elif(command == '4'):
        rosmap_menu.call_rosmap_gene_stats()

    elif(command == 'q'):
        command = False
    else:
        command = True

sys.exit()
