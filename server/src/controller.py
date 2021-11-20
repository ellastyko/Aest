from src.query import Query


class Controller:

    def __init__(self) -> None:
        self.query = Query()

    def controll(self, request : dict) -> dict:

        self.query.insert('users', {
            "login": 'ellastyko',
            "password": 'fsdfsdf',
            "key": "tokken" 
        })

        row = self.query.select('users', condition = {
            "id": 1
        })

        # print(row)

