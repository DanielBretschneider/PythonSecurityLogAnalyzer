#! /usr/bin/python3
"""
File:   py_systemd.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-07-06

Description:
    Helper file which defines systemd specific functions and methods.
    Comment will progress as the file progresses.

"""

#
# ----- IMPORTS -----
#
from systemd import journal


#
# ----- GLOBALS -----
#


#
# ----- FUNCTIONS -----
#

def write():
    """

    """
    journal.send("Hi, that's my first journald entry.")