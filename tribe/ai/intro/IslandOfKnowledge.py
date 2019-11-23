def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft != friendsLeft :
        if yourLeft != friendsRight :
            return False
        else :
            if yourRight != friendsRight and yourRight != friendsLeft :
                return False
    elif yourRight != friendsRight :
        return False
    return True

def arrayMaximalAdjacentDifference(inputArray):
    maxDiff = 0
    for i in range(0, len(inputArray)-1) :
        if abs(inputArray[i] - inputArray[i+1]) > maxDiff :
            maxDiff = abs(inputArray[i] - inputArray[i+1])
    return maxDiff

def isIPv4Address(inputString):
    str_octets = str(inputString).split(".")
    int_octets = []
    for s_octet in str_octets :
        try:
            int_octets.append(int(s_octet))
        except:
            return False
    if len(int_octets) != 4 :
        return False
    for octet in int_octets :
        if octet > 255 or octet < 0 :
            return False
    return True

def avoidObstacles(inputArray):
    inputArray.sort()
