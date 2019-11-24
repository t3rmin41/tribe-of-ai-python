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

def isIPv4Address(inputString : str) -> bool : # optional typing, return type - boolean but still works if type doesn't match
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
    return 0

def boxBlur(image):
    square_side_size = 3
    blurred_rows_num = (len(image) - square_side_size) + 1
    blurred_cols_num = (len(image[0]) - square_side_size) + 1
    blurred = [[None] * blurred_cols_num] * blurred_rows_num
    n = 0
    m = 0
    while n < blurred_rows_num :
        while m < blurred_cols_num :
            sum = 0
            count = 0
            for i in range(n, n + square_side_size) :
                for j in range(m, m + square_side_size) :
                    sum = sum + image[i][j]
                    count = count + 1
            blurred[n][m] = sum // count
            m = m + 1
            n = n + 1
    return blurred

def minesweeper(matrix):
    return matrix