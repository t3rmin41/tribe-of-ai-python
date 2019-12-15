import re
def variableName(name):
    pattern = r"^[a-zA-Z_][a-zA-Z_0-9]*"
    return bool(re.fullmatch(pattern, name))