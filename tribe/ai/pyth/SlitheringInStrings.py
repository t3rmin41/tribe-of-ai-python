def fixMessage(message):
    return message.lower().capitalize()

def catWalk(code):
    return " ".join(code.split())

def convertTabs(code, x):
    return code.replace("\t", " "*x)

import textwrap
def feedbackReview(feedback, size):
    return textwrap.wrap(feedback, size, break_long_words=False)

def isWordPalindrome(word):
    return word == word[::-1]

def permutationCipher(password, key):
    table = password.maketrans("abcdefghijklmnopqrstuvwxyz", key)
    return password.translate(table)

def competitiveEating(t, width, precision):
    return "{:^{width}.{prec}f}".format(str(round(t, precision)))

def newStyleFormatting(s):
    return str(s).replace("%", "{}")

def getCommit(commit):
    return str(commit).split("!!")
