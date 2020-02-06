def byteArrayToInt(byteArray):
    result = 0
    for x in range(len(byteArray)):
        bill = byteArray[len(byteArray)-x-1] * 256**x
        result += bill

    return result