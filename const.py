#!/bin/python3
"""
Author  :   Gaël Mariot
Date    :   20.02.2020
Name    :   const.py
Desc.   :   This file contains contants for the project
"""

APPMARK = b'\xff'
SOI_MARKER = APPMARK+b'\xd8'
EOI_MARKER = APPMARK+b'\xd9'
EXIF_APP = APPMARK+b'\xe1'
JFIF_APP = b'\xe0'

EXIF_HEADER = b'\x45\x78\x69\x66\x00\x00'

INTEL_ALIGN = b'\x49\x49\x2a\x00'
MOTORLA_ALIGN = b'\x4D\x4D\x00\x2a'

TIFF_HEADER_END_MOTOROLA = b'\x00\x00\x00\x08'

TAG_NUMBER = {
    "01 00 " : "Width",
    "01 02 " : "BitsPerSample",
    "01 06 " : "PhotometricInterpretation",
    "01 15 " : "SamplesPerPixel ",
    "01 1A " : "XResolution ",
    "01 1B " : "YResolution ",
    "01 28 " : "ResolutionUnit ",
    "01 31 " : "Software ",
    "01 10 " : "Model",
    "01 01 " : "Length",
    "01 0E " : "Image Description",
    "01 0F " : "Manufacturer",
    "87 69 " : "ExifOffset",
    "01 12 " : "Orientation",
    "01 32 " : "DateTime",
    "90 03 " : "DateTime Original",
    "92 08 " : "LightSource",
}
DATA_FORMAT_LENGTH = {
    1:1,
    2:1,
    3:2,
    4:4,
    5:8,
    6:1,
    7:1,
    8:2,
    9:4,
    10:8,
    11:4,
    12:8
}