def centuryFromYear(year):
    return year // 100 + (1 if year % 100 > 0 else 0)

year1 = 1700
year2 = 1905

#print("Century of year1 ", year1, " is ", centuryFromYear(year1))
#print("Century of year2 ", year2, " is ", centuryFromYear(year2))

def checkPalindrome(inputString):
    if len(inputString) == 1:
        return True
    middle = len(inputString) // 2
    middleOdd = len(inputString) % 2
    start = inputString[0:middle + middleOdd]
    finish = inputString[len(inputString):middle-1:-1]
    if (start == finish):
        return True
    else:
        return False

stringToCheck1 = "aabaa"
stringToCheck2 = "abba"
stringToCheck3 = "k"
stringToCheck4 = "kpk"

#print("Is '", stringToCheck1, "' a palindrome? ", checkPalindrome(stringToCheck1), sep='')
#print("Is '", stringToCheck2, "' a palindrome? ", checkPalindrome(stringToCheck2), sep='')
#print("Is '", stringToCheck3, "' a palindrome? ", checkPalindrome(stringToCheck3), sep='')
#print("Is '", stringToCheck4, "' a palindrome? ", checkPalindrome(stringToCheck4), sep='')

def adjacentElementsProduct(inputArray):
    product = inputArray[0] * inputArray[1]
    for i in range(0, len(inputArray)-1):
        tmp = inputArray[i] * inputArray[i+1]
        if tmp > product:
            product = tmp
    return product

intArray1 = [3, 6, -2, -5, 7, 3]
intArray2 = [-23, 4, -3, 8, -12]

#print("adjacentElementsProduct(intArray1) =", adjacentElementsProduct(intArray1))
#print("adjacentElementsProduct(intArray2) =", adjacentElementsProduct(intArray2))

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

#print("shape n = 2 area : ", shapeArea(2), sep = '')
#print("shape n = 3 area : ", shapeArea(3), sep = '')
#print("shape n = 4 area : ", shapeArea(4), sep = '')
#print("shape n = 5 area : ", shapeArea(5), sep = '')

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

statues1 = [6, 2, 3, 8]

#print("Statues1 needed to add =", makeArrayConsecutive2(statues1))

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

sequence1 = [1, 3, 2, 1]
sequence2 = [1, 3, 2]
sequence3 = [1, 2, 1, 2]
sequence4 = [1, 2, 3, 4, 3, 6]
sequence5 = [1, 1, 2, 3, 4, 4]
sequence6 = [10, 1, 2, 3, 4, 5]
sequence7 = [1, 2, 5, 3, 5]


print("Is sequence1 almost increasing?", almostIncreasingSequence(sequence1))
print("Is sequence2 almost increasing?", almostIncreasingSequence(sequence2))
print("Is sequence3 almost increasing?", almostIncreasingSequence(sequence3))
print("Is sequence4 almost increasing?", almostIncreasingSequence(sequence4))
print("Is sequence5 almost increasing?", almostIncreasingSequence(sequence5))
print("Is sequence6 almost increasing?", almostIncreasingSequence(sequence6))
print("Is sequence7 almost increasing?", almostIncreasingSequence(sequence7))

def catWalk(code):
    return " ".join(code.split())
