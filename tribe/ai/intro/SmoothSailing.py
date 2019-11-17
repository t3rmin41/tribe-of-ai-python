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

def reverseInParentheses(inputString):
    reversed = None
    textInBrackets = []
    while "(" in inputString:
        textInBrackets.append(inputString[::])
    return reversed