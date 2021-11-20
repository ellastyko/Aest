from src.database import Database


class Query(Database):

    def __init__(self) -> None:
        Database.__init__(self)

    
    def make(self, query, all=False, first=False):

        try:
            self.sql.execute(query)
        except:
            self.db.rollback()
        else:
            self.db.commit()



    def first(self):
        return self.sql.fetchone()


    def all(self):
        return self.sql.fetchall()


    def insert(self, table : str, data : dict, condition : dict = None):

        try:
            keys = self.__fields(data.keys()) 
            values = self.__fields(data.values()) 

            self.make(f"INSERT INTO {table}({keys}) VALUES({values})")
        except:
            print('Unable to insert data')
        else:
            print("Data was inserted")

    def update(self, table : str, fields : list, values : list, condition : dict = None):
        pass

    
    def select(self, table : str, fields : list = '*', condition : dict = None):

        fields = self.__fields(fields)
        cond = self.__condition(condition)
        print(f"SELECT {fields} FROM {table} {'WHERE' + cond}")
        try:
            self.make(f"SELECT {fields} FROM {table} {'WHERE' + cond}")
        except:
            print('Unable to select')
        else:
            return self

    
    def __condition(self, condition : dict) -> str:
        return [print(f"{field}={condition[field]} {'AND' if key != len(condition) - 1 else ''}") for key, field in enumerate(condition.keys())]

    def __fields(self, fields : list) -> str:
        return [print(i, end=",") for i in fields]