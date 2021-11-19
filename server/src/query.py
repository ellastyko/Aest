

class Query:

    def __init__(self, db) -> None:
        self.db = db
        self.sql = db.cursor()

    def make(self, query, all=False, first=False):

        try:
            self.sql.execute(query)
        except:
            self.db.rollback()
        else:
            print(self.sql.fetchall())
            self.db.commit()

            if all is True:
                return self.sql.fetchall()
            elif first is True:
                return self.sql.fetchone()
            else:
                return self.sql
