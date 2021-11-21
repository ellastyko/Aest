from src.query import Query


class Controller:

    def __init__(self) -> None:
        self.query = Query()

    def controll(self, request : dict) -> dict:

        # self.query.create('users', {
        #     "login": 'johmes',
        #     "password": 'fsdfsdf',
        #     "token": "tokken" 
        # })

        # self.query.make('SELECT login, password FROM users WHERE login="johm";')
        
        self.query.update('users', {
            'password' : 'PASSWORD'
        }, {
            "id": 1
        })


        row = self.query.select('users', ['id', 'login', 'password'], {
            "login": "johm"
        })
        print(row.all())

