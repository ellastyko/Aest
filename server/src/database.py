import sqlite3
from config import env
import pymysql
import os


class Database:

    DB_PATH = f'{os.getcwd()}/db/aest.db'
    MIGRATIONS = f'{os.getcwd()}/db/migrations.sql'

    def __init__(self) -> None:
        try:
            connection = env('DB_CONNECTION')
            if connection == 'mysql':
                self.db = pymysql.connect( 
                    host = env('DB_HOST'),
                    user = env('DB_USERNAME'), 
                    password = env('DB_PASSWORD'), 
                    db = env('DB_NAME')
                )
            elif connection == 'sqlite3': 
                self.db = sqlite3.connect(self.DB_PATH)
            elif connection == 'postgres':
                pass

            self.sql = self.db.cursor()
        except sqlite3.Error as error:
            print(f"Unable to connect to database: {error}!") 
        else:
            print('Connected')


    def migrations(self):

        try:
            sql_file = open(self.MIGRATIONS)
            sql_as_string = sql_file.read()
            self.sql.executescript(sql_as_string)
        except sqlite3.Error as error:
            print(f'Unable to make migrations:{error}')
        else:
            print('Migrations done!')
        self.db.commit()

    def __del__(self):
        print('Destruct!')
        self.db.close()


