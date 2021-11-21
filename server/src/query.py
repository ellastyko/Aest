from src.database import Database

#  Module was created to speed up development process and don't write long SQL queries 

class Query(Database):

    def __init__(self) -> None:
        Database.__init__(self)

    # Function with executing of 
    def make(self, query) -> None:

        try:
            self.sql.execute(query)
        except:
            self.db.rollback()
        else:
            self.db.commit()


    def limit(self) -> tuple: #TODO
        pass

    def first(self) -> tuple:
        return self.sql.fetchone()

    def all(self) -> list:
        return self.sql.fetchall()

    # Main operations with DB
    def create(self, table : str, data : dict, condition : dict = None) -> object:

        try:
            keys = self.__commas(data.keys(), quotes=True) 
            values = self.__commas(data.values(), quotes=True) 

            self.make(f"INSERT INTO {table}({keys}) VALUES({values})")
        except:
            print('Unable to insert data')
        else:
            print("Data was inserted")
            return self


    def update(self, table : str, data : dict, conditions : dict = None) -> object:
        
        try:
            values = self.__equality(data, condition = False)
            conditions = self.__equality(conditions)

            print(f"UPDATE {table} SET {values} {conditions}")
            self.make(f"UPDATE {table} SET {values} {conditions}") 
        except:
            print('Unable to update data')
        else:
            return self

    
    def select(self, table : str, fields : list , conditions : dict = None, limit : int = None) -> object:
      
        fields = self.__commas(fields)      
        conditions = self.__equality(conditions)

        try:
            self.make(f"SELECT {fields} FROM {table} {conditions}")
        except:
            print('Unable to select')
        else:
            return self


    # Helpers
    def __equality(self, dictionary : dict, condition : bool = True) -> str:


        string = 'WHERE ' if condition is True else ''

        for key, field in enumerate(dictionary.keys()):

            # Check up if value is string or integer/decimal
            if type(dictionary[field]) is str:
                value = f'"{dictionary[field]}"'
            else:
                value = dictionary[field]

            c = '' if key == len(dictionary) - 1 or condition is False else ' AND '

            string += f"{field}={value}{c}"


        return string


    def __commas(self, arr : list, quotes : bool = False) -> str:

        string = ''
        if quotes is False:
            for key, value in enumerate(arr):
                if key == len(arr) - 1:
                    string += value
                else:
                    string += f'{value}, '
        else:
            for key, value in enumerate(arr):
                if key == len(arr) - 1:
                    string += f'"{value}"'
                else:
                    string += f'"{value}", '


        return string
