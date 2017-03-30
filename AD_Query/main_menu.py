#---- Imports -----------------------------------------------------------------

import sys

#---- Functions ---------------------------------------------------------------

def display_menu():
    print(
"""
-------------------------------------------------------------------------------
|                                WELCOME                                      |
|                                                                             |
|                                  TO                                         |
|                                                                             |
|                       The Alzheimer's Disease Database                      |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
| Select from the following options:                                          |
|                                                                             |
| 1 - AD patient information                         (patients.csv / mySQL)   |
| 2 - Gene information       (entrez->uniprot & uniprot.xml / redis & mongo)  |
| 3 - Interacting genes                              (Biogrid.tab2 / neo4j)   |
| 4 - Gene statistics among AD patient             (Rosmap.csv / Cassandra)   |
| q - Exit program                                                            |
-------------------------------------------------------------------------------
""")
    command = input("Please select: " )

    return command
