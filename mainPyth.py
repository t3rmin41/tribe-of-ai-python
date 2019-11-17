from tribe.ai.pyth.MeetPyth import countBits, countBitsInLoop, modulus, simpleSort, baseConversion, mexFunction
from tribe.ai.pyth.SlitheringInStrings import fixMessage, catWalk

n = 4

print("countBits(n) =", countBits(n))
print("countBitsInLoop(n) =", countBitsInLoop(n))


arr1 = [2, 4, 1, 5]
print("arr1 sorted :", simpleSort(arr1))

n = 15

print("modulus(n) =", modulus(n))
print("n in HEX :", baseConversion(n, 10))

arr2 = [0, 4, 2, 3, 1, 7]
upperBound = 10

print("Minimum excludant in arr2", mexFunction(arr2, upperBound))

message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1"

print("Fixed message :", fixMessage(message))

line = "def      m   e  gaDifficu     ltFun        ction(x):"

print("Cat walk fixed line:", catWalk(line))

arr3 = [1, 2, 3, 4]

i, *rest, j = arr3

print("i =", i, "rest =", rest, "j =", j)