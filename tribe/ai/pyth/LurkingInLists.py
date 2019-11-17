def listsConcatenation(lst1, lst2):
    res = lst1
    #for e in lst2 : res.append(e)
    res.extend(lst2)
    return res
