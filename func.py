#!/bin/python3
"""
Author  :   Gaël Mariot
Date    :   20.02.2020
Name    :   func.py
Desc.   :   This file contains all the function for the project
"""

def byteArrayToInt(byteArray):
    result = 0
    for x in range(len(byteArray)):
        bill = byteArray[len(byteArray)-x-1] * 256**x
        result += bill

    return result