def centuryFromYear(year):
    return year // 100 + (1 if year % 100 > 0 else 0)

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