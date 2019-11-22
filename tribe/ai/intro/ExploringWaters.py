def alternatingSums(a):
    team1 = []
    team2 = []
    weightsOfTeams = []
    for i in range(0, len(a)) :
        if i % 2 == 0 :
            team1.append(a[i])
        else: team2.append(a[i])
    weightsOfTeams.append(sum(team1))
    weightsOfTeams.append(sum(team2))
    return weightsOfTeams

def addBorder(picture):
    lineLength = len(picture[0])
    picture.insert(0, "*" * lineLength)
    picture.append("*" * lineLength)
    i = 0
    for line in picture:
        borderedLine = "*" + line + "*"
        picture[i] = borderedLine
        i += 1
    return picture

def areSimilar(a, b):
    swapOccured = False
    for i in range(0, len(a)):
        if not a[i] == b[i] : # find on which position a[i] is not equal to b[i]
            for j in range(0, len(a)):
                if b[i] == a[j] and a[i] == b[j] : # find on which position a[j] is equal to b[i] and a[i] is equal to b[j]
                    b[i], b[j] = b[j], b[i]
                    swapOccured = True
                    break
        if swapOccured :
            break
    for k in range(0, len(a)):
        if not a[k] == b[k] :
            return False
    return True

import time
def arrayChange(inputArray):
    start_time = time.time()
    movesCount = 0
    listLengthMinusOne = len(inputArray)-1
    for i in range(0, listLengthMinusOne) :
        if not inputArray[i+1] > inputArray[i] and inputArray[i+1] <= inputArray[i] :
            diff = inputArray[i] - inputArray[i+1]
            inputArray[i+1] += diff + 1
            movesCount += diff + 1
            #while not inputArray[i+1] > inputArray[i] :
            #    inputArray[i+1] += 1
            #    movesCount += 1
        elif not inputArray[i+1] > inputArray[i] and inputArray[i+1] >= inputArray[i] :
            diff = inputArray[i] - inputArray[i + 1]
            inputArray[i] += diff + 1
            movesCount += diff + 1
            #while not inputArray[i+1] > inputArray[i] :
            #    inputArray[i] += 1
            #    movesCount += 1
    print("arrayChange() execution time %s seconds" % (time.time() - start_time))
    return movesCount

def palindromeRearranging(inputString):
    lst1 = []
    lst2 = []
    i = 0
    while i < len(inputString) :
        j = i + 1
        while j < len(inputString) :
            if inputString[i] == inputString[j] :
                lst1.append(inputString[i])
                lst2.append(inputString[j])
                inputString = inputString[0 : i : ] + inputString[i+1 : :]
                inputString = inputString[i : j : ] + inputString[j+1 : :]
                i = 0
                break
            j += 1
        i += 1
    if len(lst1) != len(lst2):
        return False
    else:
        lst1.sort()
        lst2.sort()
        for k in range(0, len(lst1)):
            if lst1[k] != lst2[k]:
                return False
    return True