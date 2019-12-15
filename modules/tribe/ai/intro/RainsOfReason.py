import re
def variableName(name):
    pattern = r"^[a-zA-Z_][a-zA-Z_0-9]*"
    return bool(re.fullmatch(pattern, name))

def alphabeticShift(inputString):
    shifted_dict = dict()
    ascii_in_number = range(65, 122)
    for i in ascii_in_number:
        shifted_dict[chr(i)] = chr(i+1)
    shifted_dict['z'] = 'a'
    outputString = []
    for c in inputString:
        outputString.append(shifted_dict.get(c))
    return "".join(outputString)