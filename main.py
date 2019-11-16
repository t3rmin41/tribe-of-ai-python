'''
xs = [()]

res = [False] * 2

if xs:
    res[0] = True
if xs[0]:
    res[1] = True

#print("res =", res)

def division(x, y):
    return x // y

x = 15
y = -4

#print("division x/y =", division(x, y))

def countBits(n):
    return n.bit_length()

def countBitsInLoop(n):
    i = 0
    while n > 0:
        n = n // 2
        i += 1
    return i

n = 4

print("countBits(n) =", countBits(n))
print("countBitsInLoop(n) =", countBitsInLoop(n))

def modulus(n):
    if isinstance(n, int) :
        return n % 2
    else:
        return -1

n = 15

#print("modulus(n) =", modulus(n))

def simpleSort(arr):
    n = len(arr)
    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr

arr1 = [2, 4, 1, 5]
print("arr1 sorted :", simpleSort(arr1))

def baseConversion(n, x):
    return hex(int(str(n), x))[2::]

#print("n in HEX :", baseConversion(n, 10))

def allLongestStrings(inputArray):
    maxLength = 0
    result = []
    for s in inputArray :
        if (len(s) > maxLength) :
            maxLength = len(s)
    for s in inputArray :
        if (len(s) == maxLength) :
            result.append(s)
    return result

arr2 = ["aba", "aa", "ad", "vcd", "aba"]

print("Max length strings :", allLongestStrings(arr2))
'''
'''
def commonCharacterCount(s1, s2):
    count = 0
    commonChars = []
    commonCharAppearances = []
    for c1 in s1 :
        if (c1 in s2 and c1 not in commonChars) :
            commonChars.append(c1)
    for char in commonChars :
        count1 = s1.count(char)
        count2 = s2.count(char)
        if count1 < count2 :
            count += count1
        else: count += count2
    return count

s1 = "aabcc"
s2 = "adcaa"

print("Common character count :", commonCharacterCount(s1, s2))

def isLucky(n):
    sum1 = 0
    sum2 = 0
    stringRepresentation = str(n)
    number = ((str(n)[:len(stringRepresentation)//2]), (str(n)[len(stringRepresentation)//2:]))
    for i in range(0, len(number[0])) :
        sum1 += int(number[0][i])
    for j in range(0, len(number[1])) :
        sum2 += int(number[1][j])
    return sum1 == sum2

n = 1230

print("isLucky(n)", isLucky(n))

'''

def sortByHeight(a):
    people = []
    for element in a :
        if element > 0 :
            people.append(element)
    people.sort()
    i = 0
    j = 0
    while i < len(a) :
        if a[i] > 0 :
            a[i] = people[j]
            j += 1
        i += 1
    return a


a = [-1, 150, 190, 170, -1, -1, 160, 180]

print("sortByHeight(a)", sortByHeight(a))

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


matrix1 = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

matrix2 = [[1,1,1,0],
           [0,5,0,1],
           [2,1,3,10]]

print("matrixElementsSum(matrix1) :", matrixElementsSum(matrix1))
print("matrixElementsSum(matrix2) :", matrixElementsSum(matrix2))
































