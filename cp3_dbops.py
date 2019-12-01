import pandas as pd
import sqlalchemy

class database:
    def __init__(self):
        self.engine = None

    def connect(self):
        self.engine = sqlalchemy.create_engine('mysql+pymysql://1hvINACOm5:k1mStgnUk3@remotemysql.com:3306/1hvINACOm5')
        return self.engine

    def update_data(self, dfname, dflist):
        dflist.to_sql(dfname, con = self.engine, if_exists = 'replace')
