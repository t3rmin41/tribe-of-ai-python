from tribe.ai.intro.JourneyBegins import *
from tribe.ai.intro.EdgeOfOcean import adjacentElementsProduct, shapeArea, makeArrayConsecutive2, almostIncreasingSequence, matrixElementsSum
from tribe.ai.intro.SmoothSailing import allLongestStrings, commonCharacterCount, isLucky, sortByHeight, reverseInParentheses
from tribe.ai.intro.ExploringWaters import alternatingSums, addBorder, areSimilar, arrayChange, palindromeRearranging
from tribe.ai.intro.IslandOfKnowledge import areEquallyStrong

'''

year1 = 1700
year2 = 1905

print("Century of year1 ", year1, " is ", centuryFromYear(year1))
print("Century of year2 ", year2, " is ", centuryFromYear(year2))

stringToCheck1 = "aabaa"
stringToCheck2 = "abba"
stringToCheck3 = "k"
stringToCheck4 = "kpk"

print("Is '", stringToCheck1, "' a palindrome? ", checkPalindrome(stringToCheck1), sep='')
print("Is '", stringToCheck2, "' a palindrome? ", checkPalindrome(stringToCheck2), sep='')
print("Is '", stringToCheck3, "' a palindrome? ", checkPalindrome(stringToCheck3), sep='')
print("Is '", stringToCheck4, "' a palindrome? ", checkPalindrome(stringToCheck4), sep='')

intArray1 = [3, 6, -2, -5, 7, 3]
intArray2 = [-23, 4, -3, 8, -12]

print("adjacentElementsProduct(intArray1) =", adjacentElementsProduct(intArray1))
print("adjacentElementsProduct(intArray2) =", adjacentElementsProduct(intArray2))

print("shape n = 2 area : ", shapeArea(2), sep = '')
print("shape n = 3 area : ", shapeArea(3), sep = '')
print("shape n = 4 area : ", shapeArea(4), sep = '')
print("shape n = 5 area : ", shapeArea(5), sep = '')

statues1 = [6, 2, 3, 8]

print("Statues1 needed to add =", makeArrayConsecutive2(statues1))

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

matrix1 = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

matrix2 = [[1,1,1,0],
           [0,5,0,1],
           [2,1,3,10]]

print("matrixElementsSum(matrix1) :", matrixElementsSum(matrix1))
print("matrixElementsSum(matrix2) :", matrixElementsSum(matrix2))

arr2 = ["aba", "aa", "ad", "vcd", "aba"]

print("Max length strings :", allLongestStrings(arr2))

s1 = "aabcc"
s2 = "adcaa"

print("Common character count :", commonCharacterCount(s1, s2))

n = 1230

print("isLucky(n)", isLucky(n))

a1 = [-1, 150, 190, 170, -1, -1, 160, 180]

print("sortByHeight(a)", sortByHeight(a1))

a2 = [50, 60, 60, 45, 70]

print("alternatingSums(a)", alternatingSums(a2))

s1 = "(bar)"
s2 = "foo(bar)baz"
s3 = "foo(bar(baz))blim"

print("reverseInParentheses[ ", s1, " ] : ", reverseInParentheses(s1), sep = '')
print("reverseInParentheses[ ", s3, " ] : ", reverseInParentheses(s2), sep = '')
print("reverseInParentheses[ ", s3, " ] : ", reverseInParentheses(s3), sep = '')

picture = ["abc",
           "ded"]
print("addBorder(", picture, ") :", end = " ")
print(addBorder(picture))
'''

a1 = [1, 2, 3]
b1 = [1, 2, 3]

a2 = [1, 2, 3]
b2 = [2, 1, 3]

a3 = [1, 2, 2]
b3 = [2, 1, 1]

a4 = [832, 998, 148, 570, 533, 455, 561, 894, 894, 147, 455, 279]
b4 = [832, 998, 148, 570, 533, 455, 561, 455, 894, 147, 894, 279]

#print("areSimilar(", a1, ",", b1, ") : ", end = "")
#print(areSimilar(a1, b1))
#print("areSimilar(", a2, ",", b2, ") : ", end= "")
#print(areSimilar(a2, b2))
#print("areSimilar(", a3, ",", b3, ") : ", end = "")
#print(areSimilar(a3, b3))
#print("areSimilar(", a4, ",", b4, ") : ", end = "")
#print(areSimilar(a4, b4))

arr1 = [1, 1, 1]
arr2 = [1, 2, 3]
arr3 = [-1000, 0, -2, 0]
#print("arrayChange(", arr1, ") : ", end = "")
#print(arrayChange(arr1))
#print("arrayChange(", arr2, ") : ", end = "")
#print(arrayChange(arr2))
print("arrayChange(", arr3, ") : ", end = "")
print(arrayChange(arr3))

s4 = "aabb"
print("palindromeRearranging(", s4, ") : ", end = "")
print(palindromeRearranging(s4))

yourLeft = 10
yourRight = 15
friendsLeft = 15
friendsRight = 10

print("areEquallyStrong(", yourLeft, ",", yourRight, ",", friendsLeft, ",", friendsRight, ") : ", end = "")
print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))