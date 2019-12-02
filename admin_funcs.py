import pandas as pd
import cp3_dbops as db
import cp3_parsing as webdata
import visualize

def update_all():
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
def visualize_all():
    dbops = db.database()
    dbops.connect()
    west, east = webdata.inspect_team_standings()
    dbops.update_data('WestTeams', west)
    dbops.update_data('EastTeams', east)
    teams = west.append(east, ignore_index = True)['TeamName'].values
    allstats = dbops.get_stat_types()
    for team in teams:
        for stat in allstats:
            teamdata = dbops.get_team_stats(stat, team)
            visualize.team_charts(teamdata, stat, team)

def video():
    dbops = db.database()
    dbops.connect()
    allstats = dbops.get_stat_types()
    visualize.process_video('DAL', allstats)
    return dbops

video()