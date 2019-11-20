#!/usr/bin/env python

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
num_teams = num_players // 5

total_rank = 0
role_dict = {
    'top': 0,
    'jungle': 0,
    'mid': 0,
    'adc': 0,
    'support': 0
}
for player in list_of_players:
    total_rank += int(rank[player[RANK]])
    role_dict[player[ROLE]] += 1

target_team_score = int(round((total_rank / num_players) * 5))
for role in role_dict:
    role_dict[role] = role_dict[role] // 5

f = open("teams.txt","w+")
num_teams_made = 0

while num_teams_made != num_teams:
    teamscore = 0
    team = None
    players = []
<<<<<<< HEAD:code/teamMatching.py

    finite_loop_num = 0
    while teamscore not in range(target_team_score - 1, target_team_score + 1) and finite_loop_num < 15000:
=======
    while teamscore not in range(target_team_score - 1, target_team_score):
>>>>>>> dc54df2dbef81e6e328e02d379039944ae68409e:code/teamMatching.py
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
        while len(current_team) < 5:
            if (len(players) == 0):
                if (len(current_team) == 5):
                    break
                else:
                    print('oops')
                    exit()
            index = random.randint(0,len(players) - 1)
            player = players[index]
            if (player[USERNAME] not in current_team) and (current_team_roles.count(player[ROLE]) <= (role_dict[player[ROLE]] + 1)):
                current_team_roles.append(player[ROLE])
                teamscore += int(rank[player[RANK]])
                current_team.append(player[USERNAME])
                players.pop(index)
            elif loop_stopper > (len(players) * 5):
                f.write('RERUN THE PROGRAM PLS, something went wrong.\n')
                exit()
            else:
                loop_stopper += 1
        finite_loop_num += 1
        team = current_team

    list_of_players = players.copy()
    if finite_loop_num >= 15000:
        f.write('RERUN THE PROGRAM PLS, something went wrong!!\n')
        break
    else:
        if team:
            f.write(str(team))
            f.write('\n')
            num_teams_made += 1
        finite_loop_num = 0

f.write('leftover players: \n')
for player in list_of_players:
    f.write(str(player))
    f.write('\n')
f.close()
