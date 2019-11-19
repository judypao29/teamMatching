from io import StringIO
import csv
import random

USERNAME = 0
RANK = 1
ROLE = 2
writer = StringIO

roles = ['top', 'jungle', 'mid', 'adc', 'support']
rank = {'iron': 1,
        'bronze': 2,
        'gold': 3,
        'platinum': 4,
        'diamond': 5,
        'masters': 6,
        'grandmasters': 7,
        'challenger': 8}

with open('players.csv') as csvfile:
        reader = csv.reader(csvfile)
        list_of_players = list(reader)
list_of_players.pop(0)

num_players = len(list_of_players)
num_teams = num_players / 5

total_rank = 0
for player in list_of_players:
    total_rank += int(rank[player[RANK]])

target_team_score = int(round((total_rank / num_players) * 5))
f = open("teams.txt","w+")
while len(list_of_players) != 0:
    teamscore = 0
    team = None
    players = []
    while teamscore not in range(target_team_score - 2, target_team_score + 2):
        players = list_of_players.copy()
        current_team_roles = []
        teamscore = 0
        current_team = []
        if len(players) == 5:
            list_of_last_players = []
            for p in players:
                list_of_last_players.append(p[USERNAME])
            f.write(str(list_of_last_players))
            players = []
            break
        loop_stopper = 0
        while len(current_team_roles) < 5:
            if (len(players) == 0):
                if (len(current_team_roles) == 5):
                    break
                else:
                    print('looks like you dont have enough players')
                    exit()
            index = random.randint(0,len(players) - 1)
            player = players[index]
            if player[ROLE] not in current_team_roles:
                current_team_roles.append(player[ROLE])
                teamscore += int(rank[player[RANK]])
                current_team.append(player[USERNAME])
                players.pop(index)
            elif loop_stopper > (len(players) * 2):
                print('looks like you dont have balanced roles')
                exit()
            else:
                loop_stopper += 1
        team = current_team

    list_of_players = players.copy()
    if team:
        f.write(str(team))
        f.write('\n')
f.close()
