import constants
import copy

players = copy.deepcopy(constants.PLAYERS)
teams_list = copy.deepcopy(constants.TEAMS)

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

teams = []
def balance_teams():
    for team in teams_list:
        team_dict = {}
        team_dict['name'] = team
        teams.append(team_dict)
    teams[0]['players'] = experienced[:3] + not_experienced[:3]
    teams[1]['players'] = experienced[3:6] + not_experienced[3:6]
    teams[2]['players'] = experienced[6:9] + not_experienced[6:9]
    return teams

def team_stats(team):
    team_name = team['name']
    total_players = len(team['players'])
    team_players = []
    team_guardians = []
    total_exp = 0
    total_not_exp = 0
    team_height = 0
    for player in team['players']:
        team_players.append(player['name'])
        team_guardians += player['guardians']
        team_height += player['height']
        if player['experience'] == True:
            total_exp += 1
        else:
            total_not_exp += 1
    avg_height = team_height / total_players
    print(f'\nTeam {team_name} Stats')
    print('-'*20)
    print(f'Total Players: {total_players}')
    print(f'Experienced Players: {total_exp}')
    print(f'Inexperienced Players: {total_not_exp}')
    print(f'Average Team Height: {avg_height} Inches\n')
    print('Players on Team:')
    print(', '.join(team_players))
    print('\nGuardians:')
    print(', '.join(team_guardians))
    return

def menu():
    header = '\nBASKETBALL TEAM STATS TOOL'
    print(header)
    print('-'*len(header))
    while True:
        print('\nMAIN MENU:\n')
        print('1 - Display Team Stats\n2 - Quit\n')
        try:
            menu_input = int(input('Select an option >>   '))
            if menu_input == 2:
                print('\nThank you for using the Basketball Team Stats Tool. Goodbye.')
                break
            elif menu_input == 1:
                while True:
                    print('\nTEAMS:\n')
                    for index, team in enumerate(teams):
                        print(index+1, ' - ', team['name'])
                    print('\n')
                    try:
                        team_input = int(input('Select a Team >>   '))
                        if team_input <= 0:
                            print('Oops! That is not a valid option. Please try again.')
                            continue
                        team_stats(teams[team_input-1])
                        print('\n\n')
                        input('Press ANY KEY to continue to MAIN MENU.')
                        print('-'*50)
                        break
                    except ValueError:
                        print('Oops! That is not a valid option. Please try again.')
                        continue
                    except IndexError:
                        print('Oops! That is not a valid option. Please try again.')
                        continue
                continue
            else:
                print('Oops! That is not a valid option. Please try again.\n')
                continue
        except ValueError:
            print('Oops! That is not a valid option. Please try again.\n')
            continue
        break
    return

if __name__ == '__main__':
    clean_data(players)
    balance_teams()
    menu()
