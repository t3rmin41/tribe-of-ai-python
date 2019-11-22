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

import re
def newStyleFormatting(s):
    return '%'.join(re.sub('%\w', '{}', part) for part in s.split('%%'))

def getCommit(commit):
    return "".join([c for c in commit if c not in "0?+!"])


