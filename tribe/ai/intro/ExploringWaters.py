def alternatingSums(a):
    team1 = []
    team2 = []
    weightsOfTeams = []
    for i in range(0, len(a)) :
        if i % 2 == 0 :
            team1.append(a[i])
        else: team2.append(a[i])
    weightsOfTeams.append(sum(team1))
    weightsOfTeams.append(sum(team2))
    return weightsOfTeams

def addBorder(picture):
    lineLength = len(picture[0])
    picture.insert(0, "*" * lineLength)
    picture.append("*" * lineLength)
    i = 0
    for line in picture:
        borderedLine = "*" + line + "*"
        picture[i] = borderedLine
        i += 1
    return picture

def areSimilar(a, b):
    #TODO: fix this algorithm
    for i in range(0, len(a)):
        if a[i] is not b[i] :
            for j in range(0, len(b)):
                if b[j] == a[i] :
                    b[i], b[j] = b[j], b[i]
            break
        break
    for k in range(0, len(a)):
        if (a[k] is not b[k]):
            return False
    return True