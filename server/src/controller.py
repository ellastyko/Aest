from src.query import Query


class Controller:

    def __init__(self, db) -> None:
        self.db = Query(db)

    def controll(self, action):
        print(action)