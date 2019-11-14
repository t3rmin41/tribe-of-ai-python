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
def commonCharacterCount(s1, s2):
    count = 0
    commonChars = []
    for c1 in s1 :
        if (c1 not in commonChars) :
            commonChars.append(c1)
        for c2 in s2:
            if (c2 in commonChars):
                count += 1
    return count

s1 = "aabcc"
s2 = "adcaa"

print("Common character count :", commonCharacterCount(s1, s2))
'''