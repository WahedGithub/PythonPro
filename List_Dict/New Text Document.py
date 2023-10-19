players = {} #empty dict

fobj = open("players.txt", "r")

for line in fobj: #line is a list
    fields = line.split() #assigning fields as variable to line to split

    player = fields[0]
    score = int(fields[1]) # int to convert the string

    if player in players: # here its checking the dict which is empty so it going to else part
        players[player] = players[player] + score

    else:
        players[player] = score# all the not present things will come under this


for player in players:
    print (player, end=" ")
    print (players[player])
    
