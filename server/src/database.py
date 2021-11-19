import sqlite3
import glob, os


class Database:

    DB_PATH = 'db/aest.db'
    TABLES_PATH = 'db/'
    # SQL_SCRIPTS = glob.glob(f"{os.getcwd()}\\db\\*.sql")

    def __init__(self) -> None:

        self.db = sqlite3.connect(self.PATH)
        self.sql = self.db.cursor()


    def query(self, query, all=False, first=False):

        try:
            self.sql.execute(query)
        except:
            self.db.rollback()
        else:
            self.db.commit()

            if all is True:
                return self.sql.fetchall()
            elif first is True:
                return self.sql.fetchone()
            else:
                return None


    def migrations(self):
        # TODO
        pass
        # for file in self.SQL_SCRIPTS:
        #     sql_file = open(file)
        #     sql_as_string = sql_file.read()
        #     self.sql.executescript(sql_as_string)
        
    def __del__(self):
        self.sql.close()
