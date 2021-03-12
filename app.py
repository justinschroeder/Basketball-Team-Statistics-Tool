"""
Meets Expectations:
1. Create New Script called app.py - Done
2. Use Dunder Main to prevent execution on import
3. Import PLAYERS from constants.py
4. Create clean_data function
5. Create balance_teams function
6. Ensure Console Readability
7. Display Team stats

Exceeds:
1. Clean gaurdians in clean_data
2. Balance by player exp in balance_teams
3. Include additional stats
4. Quit Menu Option

"""

import constants
import copy

players = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)

experienced = []
not_experienced = []

def clean_data(list):
    for dict in list:
        dict['guardians'] = dict['guardians'].split(' and ')
        dict['height'] = int(dict['height'].split()[0])
        if dict['experience'] == 'YES':
            dict['experience'] = True
            experienced.append(dict)
        else:
            dict['experience'] = False
            not_experienced.append(dict)
    return list

def balance_teams():
    teams[0] = experienced[:3] + not_experienced[:3]
    teams[1] = experienced[3:6] + not_experienced[3:6]
    teams[2] = experienced[6:9] + not_experienced[6:9]
    return teams

def menu():
    return

if __name__ == '__main__':
    clean_data(players)
    balance_teams()
    print(teams)
