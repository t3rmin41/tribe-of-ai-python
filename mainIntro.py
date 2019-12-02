from tribe.ai.intro.JourneyBegins import *
from tribe.ai.intro.EdgeOfOcean import adjacentElementsProduct, shapeArea, makeArrayConsecutive2, almostIncreasingSequence, matrixElementsSum
from tribe.ai.intro.SmoothSailing import allLongestStrings, commonCharacterCount, isLucky, sortByHeight, reverseInParentheses
from tribe.ai.intro.ExploringWaters import alternatingSums, addBorder, areSimilar, arrayChange, palindromeRearranging
from tribe.ai.intro.IslandOfKnowledge import areEquallyStrong, isIPv4Address, avoidObstacles, boxBlur, minesweeper

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
arr4 = [22121, 42080, -51776, -28528, 39895, -50842, 25463, 46187, -29518, 42293, -25615, -47412, 24945, -2630, -12717, -23773, -47824, -7768, -23620, -30270, -51644, 42829, 27609, -40734, 2142, 20285, 29665, -36557, -24074, -11996, 30511, 17104, 4360, -41163, 6814, 959, 26613, -15121, -17355, 28424, -11305, 33175, -8585, 23649, -18428, 16770, 14095, 38766, -22425, -45139, -5836, -28668, -15123, -35450, 41353, 11103, -29233, -51990, -14958, 45944, 20841, -34149, 34720, -51760, 23519, -46257, 40985, -32615, -43378, 14243, -24731, 1311, -4236, -24885, 41713, -45195, -14683, 47765, 26904, -51741, 38051, 13429, 38189, -45812, -52474, 14936, 6582, -26313, 4692, 12313, -37502, -40673, 5799, 23264, 33617, -50938, 26268, -25548, -22353, -15175, -21568, 18656, 19208, 20674, 41228, -42538, -45085, -32356, -39901, -39585, -50690, 2859, -4079, 29823, 28849, -2142, -16613, 23378, 36363, 31780, -40379, 7489, -13324, -22377, 35661, -27141, -42727, 10122, -40385, -19765, 33913, -10504, -4715, -18190, 41430, -19134, 32646, 25839, 783, 32941, -25142]

#print("arrayChange(", arr1, ") : ", end = "")
#print(arrayChange(arr1))
#print("arrayChange(", arr2, ") : ", end = "")
#print(arrayChange(arr2))
print("arrayChange(", arr3, ") : ", end = "")
print(arrayChange(arr3))
print("arrayChange( arr4 ) : ", end = "")
print(arrayChange(arr4))

s4 = "accababa"
#print("palindromeRearranging(", s4, ") : ", end = "")
#print(palindromeRearranging(s4))

s5 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
#print("palindromeRearranging(", s5, ") : ", end = "")
#print(palindromeRearranging(s5))

s6 = "abbcabb"
#print("palindromeRearranging(", s6, ") : ", end = "")
#print(palindromeRearranging(s6))


yourLeft = 10
yourRight = 15
friendsLeft = 15
friendsRight = 10

#print("areEquallyStrong(", yourLeft, ",", yourRight, ",", friendsLeft, ",", friendsRight, ") : ", end = "")
#print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))

ipv4_1 = "172.16.254.1"
ipv4_2 = "172.316.254.1"
ipv4_3 = ".254.255.0"
ipv4_4 = 100

#print("isIPv4Address(", ipv4_1, ") : ", end = "")
#print(isIPv4Address(ipv4_1))

#print("isIPv4Address(", ipv4_2, ") : ", end = "")
#print(isIPv4Address(ipv4_2))


#print("isIPv4Address(", ipv4_3, ") : ", end = "")
#print(isIPv4Address(ipv4_3))

#print("isIPv4Address(", ipv4_4, ") : ", end = "")
#print(isIPv4Address(ipv4_4))

inputArray1 = [5, 3, 6, 7, 9]
inputArray2 = [1, 4, 10, 6, 2]
#print("avoidObstacles(", inputArray1, ") : ", end = "")
#print(avoidObstacles(inputArray1))
print("avoidObstacles(", inputArray2, ") : ", end = "")
print(avoidObstacles(inputArray2))

image1 = [[1, 2, 3],
         [1, 7, 4],
         [1, 3, 2]]
#print("boxBlur(", image1, ") : ", end = "")
#print(boxBlur(image1))

image2 = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]
#print("boxBlur(", image2, ") : ", end = "")
#print(boxBlur(image2))

image3 = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]
#print("boxBlur(", image3, ") : ", end = "")
#print(boxBlur(image3))

matrix1 = [[True, False, False],
          [False, True, False],
          [False, False, False]]
#print("minesweeper(", matrix1, ") : ", end = "")
#print(minesweeper(matrix1))