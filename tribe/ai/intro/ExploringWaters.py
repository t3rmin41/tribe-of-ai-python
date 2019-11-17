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