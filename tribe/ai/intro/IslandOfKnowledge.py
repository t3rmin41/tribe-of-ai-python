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

def isIPv4Address(inputString : str) -> bool : # optional typing, return type - boolean but still execution continues if type doesn't match
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
    #blurred = [[None] * blurred_cols_num] * blurred_rows_num # this line doesn't produce rows X cols matrix but reuses list objects multiple times
    # this means that each row points at the same place in memory and when 0-th column is changed at 0-th row the value of 0-th column changes for all rows, not just 0-th
    blurred = [[None for i in range(0, blurred_cols_num)] for j in range(0, blurred_rows_num)] # the correct way to produce rows X cols matrix
    n = 0
    while n < blurred_rows_num :
        m = 0
        while m < blurred_cols_num :
            sum = 0
            count = 0
            for i in range(n, n + square_side_size) :
                for j in range(m, m + square_side_size) :
                    sum = sum + image[i][j] # getting matrix's element at i row at j column is OK
                    count = count + 1
            blurred[n][m] = sum // count # how to assign value to n-th list m-th element?
            m = m + 1
        n = n + 1
    return blurred

def minesweeper(matrix):
    minesweeped_matrix = [[None for i in range(0, len(matrix[0]))] for j in range(0, len(matrix))]
    for i in range(0, len(minesweeped_matrix)):
        for j in range(0, len(minesweeped_matrix[i])) :
            neighboring_cell = 0
            if i > 0 and j > 0 and i < len(minesweeped_matrix) and j < len(minesweeped_matrix[i]) : # the cell has all 8 neighbors, angle neighbors are also counted
                if matrix[i][j-1] :
                    neighboring_cell += 1
                if matrix[i][j+1] :
                    neighboring_cell += 1
                if matrix[i-1][j] :
                    neighboring_cell += 1
                if matrix[i+1][j] :
                    neighboring_cell += 1
    return minesweeped_matrix