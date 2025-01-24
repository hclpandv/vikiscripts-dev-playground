#!/usr/bin/env python
"""cli program to get os info"""
import os

def get_os_info():
    """
    Function to get os info
    """
    output = os.getcwd()
    return output

print(get_os_info())
