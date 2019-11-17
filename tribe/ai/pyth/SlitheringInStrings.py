def fixMessage(message):
    return message.lower().capitalize()

def catWalk(code):
    return " ".join(code.split())

def convertTabs(code, x):
    return code.replace("\t", " "*x)
