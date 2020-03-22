from class_E.modules.tribe.ai.pyth.MeetPyth import countBits, countBitsInLoop, modulus, simpleSort, baseConversion, mexFunction
from class_E.modules.tribe.ai.pyth.SlitheringInStrings import fixMessage, catWalk, convertTabs, \
    feedbackReview, isWordPalindrome, permutationCipher, competitiveEating, newStyleFormatting, getCommit, getNumericsFromString
from class_E.modules.tribe.ai.pyth.LurkingInLists import listsConcatenation, twoTeams, removeTasks
from class_E.modules.tribe.ai.pyth.LambdaIllusions import getPoints

'''
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

arr3 = [3, 4, 2, 4, 38, 4, 5, 3, 2]
print("arr3 =", arr3)
i, *rest, j = arr3
print("i =", i, "rest =", rest, "j =", j)

message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1"
print("Fixed message :", fixMessage(message))

line = "def      m   e  gaDifficu     ltFun        ction(x):"
print("Cat walk fixed line:", catWalk(line))

c = "\treturn False"
x = 4
print("convertTabs(", c , ") =", convertTabs(c, x))

feed = "This is an example feedback"
size = 8
print("feedbackReview[", feed, ", ", size, "]", feedbackReview(feed, size))

word1 = "aibohphobia"
word2 = "hehehehehe"
print("isWordPalindrome[", word1, "]", isWordPalindrome(word1))
print("isWordPalindrome[", word2, "]", isWordPalindrome(word2))

password = "iamthebest"
key = "zabcdefghijklmnopqrstuvwxy"
print("permutationCipher[", password, ",", key, "]", permutationCipher(password, key))

t = 3.1415
width = 10
precision = 2
#print("competitiveEating[", t, ",", width, ",", precision, "]", competitiveEating(t, width, precision))

s1 = "We expect the %f%% growth this week"
s2 = "%d%d%%-growth in products is expected quite soon"
print("newStyleFormatting[", s1, "] :", newStyleFormatting(s1))
print("newStyleFormatting[", s2, "] :", newStyleFormatting(s2))

commit = "0??+0+!!someCommIdhsSt"
print("getCommit[", commit, "] :", getCommit(commit))

'''

#lst1 = [2, 2, 1]
#lst2 = [10, 11]
#print("listsConcatenation(", lst1, ",", lst2, ") :", listsConcatenation(lst1, lst2))

#students1 = [1, 11, 13, 6, 14]
#print("twoTeams(", students1, ") :", twoTeams(students1))

k = 3
toDo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22]
print("removeTasks(", k, ",", toDo, ") :", end="")
print(removeTasks(k, toDo))

ch = "*"
n = 10

repeatChar = lambda ch, n: ch * n

#print("repeatChar(", ch, ",", n, ") :", repeatChar(ch, n))

str1 = "There are over 100'000.00 USD in cash and also 200'000 $ in the account"
str2 = "There are over 100 000,00 EUR in cash but only 100,00 in the account"

amount1 = getNumericsFromString(str1)
#print("amount1 :", amount1)
amount2 = getNumericsFromString(str2)
#print("amount2 :", amount2)

#generator comprehension, enumerate  - for TwoTeams task
#for RemoveTasks - del

answers1 = [True, True, False, True]; p = 2
print("getPoints(", answers1, ",", p, ") : ", end="")
print(getPoints(answers1, p))