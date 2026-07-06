#! /usr/bin/python3
"""
File:   main.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-07-06

Description:
    Main file in this project. This description is still in progress.

Info:
    Uses py_systemd.py as helper for systemd specific tasks.

"""

#
# ----- IMPORTS -----
#
from py_systemd import write

#
# ----- GLOBALS -----
#


#
# ----- FUNCTIONS -----
#

def main():
    """
    Entry point of whole project.
    """
    write()


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()