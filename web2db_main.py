import pandas as pd
import cp3_dbops as db
import cp3_parsing as webdata


def main():
    dbops = db.database()
    dbops.connect()
    west, east = webdata.inspect_team_standings()
    dbops.update_data('WestTeams', west)
    dbops.update_data('EastTeams', east)
    teams = west.append(east, ignore_index = True)['TeamName'].values
    teamtable = webdata.inspect_teams(teams)
    dbops.update_data('AllTeams', teamtable)
    seasontable = webdata.standings_by_season()
    dbops.update_data('AllSeasons', seasontable)
