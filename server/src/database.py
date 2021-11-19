import sqlite3
import os


class Database:

    DB_PATH = f'{os.getcwd()}/db/aest.db'
    SQL_PATH = f'{os.getcwd()}/db/script.sql'

    def __init__(self) -> None:
        pass

    def connect(self):
        try:
            self.db = sqlite3.connect(self.DB_PATH)
        except:
            print("Unable to connect to database") 
        else:
            print('Connected')
        
        return self.db


    def migrations(self):
        self.sql = self.db.cursor()
        try:
            sql_file = open(self.SQL_PATH)
            sql_as_string = sql_file.read()
            print(sql_as_string)
            self.sql.executescript(sql_as_string)
        except:
            print('Unable to make migrations')
        else:
            print('Migrations done')
        self.sql.close()

        
    def __del__(self):
        self.sql.close()
