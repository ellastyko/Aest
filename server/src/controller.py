
from config import env
from src.email import Email

class Controller:

    def __init__(self) -> None:
        self.email = Email()

    def __call__(self, request : dict) -> dict:
        # return { 'code' : 200 }

        if request['action'] == 'login':
            pass
        if request['action'] == 'login':
            pass
         # self.query.create('users', {
        #     "login": 'johmes',
        #     "password": 'fsdfsdf',
        #     "token": "tokken" 
        # })

        # print(self.query.make('SELECT users FROM INFORMATION_SCHEMA.TABLES').first())
        
        # self.query.update('users', {
        #     'password' : 'PASSWORD'
        # }, {
        #     "id": 1
        # })


        # row = self.query.select('users', ['id', 'login', 'password'], {
        #     "login": "johm"
        # })

        # variable = {key:val for key,val in row.all()}
        # print(variable)

