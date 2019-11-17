def adjacentElementsProduct(inputArray):
    product = inputArray[0] * inputArray[1]
    for i in range(0, len(inputArray)-1):
        tmp = inputArray[i] * inputArray[i+1]
        if tmp > product:
            product = tmp
    return product

def shapeArea(n):
    if n < 1:
        return 0
    areaCrossPart = 4*n - 4 + 1
    areaAddedSquares = 0
    i = 2
    while (n - i > 0) :
        areaAddedSquares += n - i
        i += 1
    return areaCrossPart + areaAddedSquares * 4

def makeArrayConsecutive2(statues):
    statues.sort()
    consecutivesNeeded = 0
    i = 0
    while i < len(statues)-1:
        while statues[i]+1 != statues[i+1]:
            statues[i] += 1
            consecutivesNeeded += 1
        i += 1
    return consecutivesNeeded

def almostIncreasingSequence(sequence):
    countElementsToRemove = 0
    copySequence = None
    i = 0
    while i < len(sequence)-1:
        if sequence[i] >= sequence[i+1] :
            if countElementsToRemove == 0 :
                copySequence = sequence.copy()
            countElementsToRemove += 1
            del sequence[i+1]
        i += 1
    i = 0
    while i < len(sequence) -1 :
        if sequence[i] >= sequence[i+1] :
            countElementsToRemove += 1
        i += 1
    if countElementsToRemove < 2 :
        return True
    else :
        countElementsToRemove = 0
        i = 0
        while i < len(copySequence)-1 :
            if copySequence[i] >= copySequence[i+1] :
                countElementsToRemove += 1
                del copySequence[i]
            i += 1
        i = 0
        while i < len(copySequence) - 1:
            if copySequence[i] >= copySequence[i + 1]:
                countElementsToRemove += 1
            i += 1
    return not (countElementsToRemove > 1)

def matrixElementsSum(matrix):
    sum = 0
    score = 0
    lowerThanScoreFound = False
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i == 0 :
                sum += matrix[i][j]
            if i > 0 :
                k = 0
                while k < i:
                    if matrix[k][j] <= score :
                        lowerThanScoreFound = True
                    k += 1
                if not lowerThanScoreFound :
                    sum += matrix[i][j]
                lowerThanScoreFound = False
    return sum