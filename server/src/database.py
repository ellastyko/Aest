import sqlite3
import os


class Database:

    DB_PATH = f'{os.getcwd()}/db/aest.db'
    SQL_PATH = f'{os.getcwd()}/db/script.sql'

    def __init__(self) -> None:
        try:
            self.db = sqlite3.connect(self.DB_PATH)
            self.sql = self.db.cursor()
        except:
            print("Unable to connect to database") 
        else:
            print('Connected')


    def migrations(self):

        try:
            sql_file = open(self.SQL_PATH)
            sql_as_string = sql_file.read()
            self.sql.executescript(sql_as_string)
        except:
            print('Unable to make migrations')
        else:
            print('Migrations done')
        self.db.commit()

    def __del__(self):
        print('destruct!!!')
        self.db.close()


