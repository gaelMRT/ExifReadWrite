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
    

    if(byteArray[:2] != SOI_MARKER):
        print("\"%s\" is not a JPG File" % (filename))
    else:
        if(byteArray[2:4] != EXIF_APP):
            print("\"%s\" does not contain exif" % (filename))
        else:
            print("\"%s\" is a jpg with exif" % filename)
            SIZE = byteArrayToInt(byteArray[4:6])

            print("Size of exif : %d bytes" % SIZE)

            EXIFHEADER = byteArray[4:SIZE+4]

            if(EXIFHEADER[2:8] == EXIF_HEADER):
                print("Exif header confirmed")

            #Check the alignments of bytes (Intel give the lightest byte at left, Motorola is the inverse)
            MotorlaAlign = EXIFHEADER[8:12] == MOTORLA_ALIGN
            IntelAlign = EXIFHEADER[8:12] == INTEL_ALIGN
            if(MotorlaAlign):
                print("It is in Motorola byte align")
            if(IntelAlign):
                print("Yeet! See ya fuckers!")
                exit()
            
            print(byteArrayToStr(EXIFHEADER[12:16]))
            IFDOffset = byteArrayToInt(EXIFHEADER[12:16])
            print("Offset pour IFD = %d"  % IFDOffset)

            #READ IFD
            
            nbDirectories = byteArrayToInt(EXIFHEADER[16:18])
            print("Number of directories : %d" % nbDirectories)

            actualId = 18

            datasOffseted = {}
            for x in range(nbDirectories):
                print("Directory %d" % x)
                tag = TAG_NUMBER[byteArrayToStr(EXIFHEADER[actualId:actualId+2])]
                dataLength = DATA_FORMAT_LENGTH[byteArrayToInt(EXIFHEADER[actualId+2:actualId+4])]
                nbComponents = byteArrayToInt(EXIFHEADER[actualId+4:actualId+8])
                dataValue = EXIFHEADER[actualId+8:actualId+12]

                if(nbComponents * dataLength > 4):
                    print("Tag = %s - length %d - nb %d - offset %d" %(tag,dataLength,nbComponents,byteArrayToInt(dataValue)))
                    datasOffseted[tag] = (dataLength*nbComponents)
                else:
                    print("Tag = %s - length %d - nb %d - value %s = %d" %(tag,dataLength,nbComponents,byteArrayToStr(dataValue),byteArrayToInt(dataValue)))
                actualId += 12
            offsetNextIFD =byteArrayToInt(EXIFHEADER[actualId:actualId+4]) 
            actualId+=4
            print("Next IFD : %d " %offsetNextIFD)

            for x in datasOffseted:
                print("%s = %s" % (x,byteArrayToWord(EXIFHEADER[actualId:actualId+datasOffseted[x]])))
                actualId += datasOffseted[x]
            print(byteArrayToStr(EXIFHEADER[actualId:]))

            #READ EXIF IFD

            nbDirectories = byteArrayToInt(EXIFHEADER[actualId:actualId+2])
            print("Number of directories : %d" % nbDirectories)

            actualId+=2
            datasOffseted = {}
            for x in range(nbDirectories):
                print("Directory %d" % x)
                tag = TAG_NUMBER[byteArrayToStr(EXIFHEADER[actualId:actualId+2])]
                dataLength = DATA_FORMAT_LENGTH[byteArrayToInt(EXIFHEADER[actualId+2:actualId+4])]
                nbComponents = byteArrayToInt(EXIFHEADER[actualId+4:actualId+8])
                dataValue = EXIFHEADER[actualId+8:actualId+12]

                if(nbComponents * dataLength > 4):
                    print("Tag = %s - length %d - nb %d - offset %d" %(tag,dataLength,nbComponents,byteArrayToInt(dataValue)))
                    datasOffseted[tag] = (dataLength*nbComponents)
                else:
                    print("Tag = %s - length %d - nb %d - value %s = %d" %(tag,dataLength,nbComponents,byteArrayToStr(dataValue),byteArrayToInt(dataValue)))
                actualId += 12
            offsetNextIFD =byteArrayToInt(EXIFHEADER[actualId:actualId+4]) 
            actualId+=4
            print("Next IFD : %d " %offsetNextIFD)

            for x in datasOffseted:
                print("%s = %s" % (x,byteArrayToWord(EXIFHEADER[actualId:actualId+datasOffseted[x]])))
                actualId += datasOffseted[x]
            print(byteArrayToStr(EXIFHEADER[actualId:]))


            nbDirectories = byteArrayToInt(EXIFHEADER[actualId:actualId+2])
            print("Number of directories : %d" % nbDirectories)

            actualId+=2
            datasOffseted = {}
            for x in range(nbDirectories):
                print("Directory %d" % x)
                tag = TAG_NUMBER[byteArrayToStr(EXIFHEADER[actualId:actualId+2])]
                dataLength = DATA_FORMAT_LENGTH[byteArrayToInt(EXIFHEADER[actualId+2:actualId+4])]
                nbComponents = byteArrayToInt(EXIFHEADER[actualId+4:actualId+8])
                dataValue = EXIFHEADER[actualId+8:actualId+12]

                if(nbComponents * dataLength > 4):
                    print("Tag = %s - length %d - nb %d - offset %d" %(tag,dataLength,nbComponents,byteArrayToInt(dataValue)))
                    datasOffseted[tag] = (dataLength*nbComponents)
                else:
                    print("Tag = %s - length %d - nb %d - value %s = %d" %(tag,dataLength,nbComponents,byteArrayToStr(dataValue),byteArrayToInt(dataValue)))
                actualId += 12
            offsetNextIFD =byteArrayToInt(EXIFHEADER[actualId:actualId+4]) 
            actualId+=4
            print("Next IFD : %d " %offsetNextIFD)

            for x in datasOffseted:
                print("%s = %s" % (x,byteArrayToWord(EXIFHEADER[actualId:actualId+datasOffseted[x]])))
                actualId += datasOffseted[x]
            print(byteArrayToStr(EXIFHEADER[actualId:]))



            REMAINING = byteArray[SIZE+4:]
