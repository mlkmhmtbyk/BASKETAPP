import pandas as pd
import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase

def inspect_players():
    table = pd.DataFrame()
    for c in ascii_lowercase:
        if c is not 'x':
            table = table.append(pd.read_html('http://www.basketball-reference.com/players/' + c + '/')[0], ignore_index=True)
            print("Parsing Player Statistics - Page " + c)
            
    print(table)
    return table
def inspect_teams(team_list):
    allteams = pd.DataFrame()
    for team in team_list:
        print("Parsing Team Statistics - Team: ", team)
        r = requests.get('http://www.basketball-reference.com/teams/'+team+'/2020.html')
        soup = BeautifulSoup(r.text, "html.parser")
        filtered = soup.find('div', id='all_totals')
        table_data = ""
        for x in filtered:
            table_data = table_data + str(x)
    
        table=pd.read_html(table_data)[0]
        table = table.rename(columns={'Unnamed: 1': 'PlayerName'})
        table = table.drop(len(table) - 1, axis = 0)
        table['TeamName'] = team
        allteams = allteams.append(table, ignore_index = True)

        
    return allteams
def inspect_team_standings():
    tables = pd.read_html('http://www.basketball-reference.com')
    easttable = tables[0].drop(['Unnamed: 1', 'Unnamed: 2'], axis = 1)
    westtable = tables[1].drop(['Unnamed: 1', 'Unnamed: 2'], axis = 1)

    westteams = westtable['West'].str.slice(stop=3)
    westtable = westtable.drop('West', axis = 1)
    westtable['TeamName'] = westteams

    eastteams = easttable['East'].str.slice(stop=3)
    easttable = easttable.drop('East', axis = 1)
    easttable['TeamName'] = eastteams

    return westtable, easttable
def standings_by_season():
    allseasons = pd.DataFrame()
    season = 2020
    for i in range(5):
        season = 2020 - i
        table = pd.read_html('https://www.basketball-reference.com/leagues/NBA_' + str(season) +'_standings.html')[0]
        print("Parsing Season Standings - Season: " + str(season))
        table['Year'] = season
        allseasons = allseasons.append(table, ignore_index = True)

    return allseasons
