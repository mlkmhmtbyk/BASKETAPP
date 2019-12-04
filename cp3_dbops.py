import pandas as pd
import pymysql
import sqlalchemy

class database:
    def __init__(self):
        self.engine = None
        self.connection = None
    def connect(self):
        self.engine = sqlalchemy.create_engine('mysql+pymysql://1hvINACOm5:k1mStgnUk3@remotemysql.com:3306/1hvINACOm5')
        self.connection = pymysql.connect(host='remotemysql.com',
                                          user='1hvINACOm5',
                                          password = 'k1mStgnUk3',
                                          db='1hvINACOm5',
                                          port=3306)
        return self.engine
    def update_data(self, dfname, dflist):
        dflist.to_sql(dfname, con = self.engine, if_exists = 'replace')

    def get_player_stats(self, playername):
        with self.connection.cursor() as cursor:
            # Read a single record
            f = open("player_stats_sql.txt", "r")
            sql = f.read() + "'" + playername + "'"
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result) == 0:
                print("Player not found, or he is not currently playing for any team.")
                return None
            else:
                result = result[0]
                player_table = pd.DataFrame(result, index = ['TotalFG%',
                                                             '3PointFG%',
                                                             'EffectiveFG%',
                                                             '2PointFG%',
                                                             'FreeThrows%',
                                                             'Rebounds',
                                                             'Assists',
                                                             'Steals',
                                                             'Blocks',
                                                             'Turnovers',
                                                             'Fauls'], columns=[playername])
                print(player_table)
                return player_table
    def get_team_stats(self, gameterm, teamname):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT PlayerName, {} FROM `AllTeams` WHERE TeamName = %s".format("`" + gameterm+ "`")
            cursor.execute(sql, (teamname))
            
            result = list(cursor.fetchall())
            
            if len(result) == 0:
                print("Keyword not found.")
                return None
            else:
                
                team_table = pd.DataFrame(result, columns=['PlayerName',gameterm])
                print(team_table)
                return team_table
    def get_stat_types(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'AllTeams'"
            cursor.execute(sql)
            
            result = list(cursor.fetchall())
            
            if len(result) == 0:
                print("No data.")
                return None
            else:
                
                team_table = pd.DataFrame(result)
                print(team_table[3])
                return team_table[3].drop([1,4,10,12,15,19,23,25,27], axis = 0).values
