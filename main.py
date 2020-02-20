#!/bin/python3
"""
Author  :   Gaël Mariot
Date    :   20.02.2020
Name    :   main.py
Desc.   :   This file is the main part of the project and is meant to be executed
"""

import sys
from func import *
from const import *

allFiles = ["w.jpg"]

for filename in allFiles:
    f = open(filename,"rb")
    freaded = f.read()
    f.close()

    byteArray = bytearray(freaded)
    stringArray = str(freaded)

    if(byteArray[:2] != JPG_MARKER):
        print("\"%s\" is not a JPG File" % (filename))
    else:
        if(byteArray[2:4] != APPMARK+EXIF_APP):
            print("\"%s\" does not contain exif" % (filename))
        else:
            print("\"%s\" is a jpg with exif" % filename)
            SIZE = byteArrayToInt(byteArray[4:6])

            print("Size of exif : %d bytes" % SIZE)

            EXIFHEADER = byteArray[4:SIZE+4]

            REMAINING = byteArray[SIZE+4:]


            exifTot = ""
            for x in EXIFHEADER:
                exifTot += ("%02X " % x)
            print(exifTot)

            remainingTot = ""
            for x in REMAINING:
                remainingTot += ("%02X " % x)
            print(len(freaded))