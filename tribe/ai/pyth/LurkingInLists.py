def listsConcatenation(lst1, lst2):
    res = lst1
    #for e in lst2 : res.append(e)
    res.extend(lst2)
    return res

def twoTeams(students):
    return sum([students[i] for i in range(0, len(students)) if i % 2 == 0]) - sum([students[i] for i in range(0, len(students)) if i % 2 == 1])

def removeTasks(k, toDo):
    del toDo[k-1::k]
    return toDo
