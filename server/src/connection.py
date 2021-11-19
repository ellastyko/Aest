from threading import  Thread, current_thread, main_thread
import socket
from src.database import Database
from src.controller import Controller
from config import env


class Connection:

        users = []

        def __init__(self):   

            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
            self.server.bind(('', env('PORT')))
            self.server.listen(10)
            print("Server listening...")

            self.__accept_sockets()
            

        def send(self, data):
            for user in self.users:
                user.send(data.encode('utf-8'))


        def __listening(self, client_socket, db):

            print("Listening user...\n")
            controller = Controller(db)
            while True:

                if main_thread().is_alive() is not True:
                    return 0             

                data = client_socket.recv(2048).decode('utf-8')
                if not data:
                    print(f"User {client_socket} disconnected!")
                    break

                controller.controll(data)

            client_socket.close()


        def __accept_sockets(self):

            db = Database().connect()

            while True:
                client_socket, client_address = self.server.accept()
                print('Connected by', client_address)

                self.users.append(client_socket)

                listen_accepted_user = Thread(target=self.__listening, args=(client_socket, db,))
                listen_accepted_user.start()
