import sys
from func import *


filename = "w.jpg"

f = open(filename,"rb")

freaded = f.read()
f.close()

byteArray = bytearray(freaded)

if(byteArray[:2] != '\xff\xd8'):
    print("Not a JPG File")
if(byteArray[2:4] != '\xff\xe1'):
    print("Not an exif file")
    exit()

SIZE = byteArrayToInt(byteArray[4:6])

print("Size of exif : %d bytes" % SIZE)

EXIFHEADER = byteArray[4:SIZE+4]

REMAINING = byteArray[SIZE+4:]


for x in EXIFHEADER:
    sys.stdout.write("%02X " % x)
print("")
print(EXIFHEADER)

for x in REMAINING[:10]:
    sys.stdout.write("%02X " % x)
print("")
print(REMAINING[:10])