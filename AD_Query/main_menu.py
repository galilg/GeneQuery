#---- Imports -----------------------------------------------------------------

import sys

#---- Functions ---------------------------------------------------------------

def display_menu():
    print(
"""
------------------------------------------------------------------------------|
|                                WELCOME                                      |
|                                                                             |
|                                  TO                                         |
|                                                                             |
|                                                                             | |                     The Alzheimer's Disease Database                        |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
| Select from the following options:                                          |
|                                                                             |
| 1 - AD patient information                                                  |
| 2 - Gene information                                                        |
| 3 - Interacting genes                                                       |
| 4 - Gene statistics among AD patients                                       |
| 5 - Exit program                                                            |
-------------------------------------------------------------------------------
""")
    command = input("Please select: " )

    return command
