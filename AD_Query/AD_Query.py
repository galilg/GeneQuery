#!/usr/bin/python /usr/bin/env

#---- Imports -----------------------------------------------------------------

import lib.biogrid.Biogrid as bio
import lib.rosmap.RNA_data as rna
import rosmap_menu
from main_menu import display_menu

import sys

#---- Main --------------------------------------------------------------------
rna_data = rna.RNA_data()
biogrid = bio.Biogrid()

#import pdb; pdb.set_trace()
command = True
while(command):
    command = display_menu()
    if (command == '1'):
        # Call patient info module
        pass
    elif(command == '2'):
        # Call gene info module
        pass
    elif(command == '3'):
        # Call interacting genes
        pass
    elif(command == '4'):
        # Call gene stats
        rosmap_menu.call_rosmap_gene_stats()
        pass
    elif(command == '5'):
        command = False
    else:
        command = True

sys.exit()
