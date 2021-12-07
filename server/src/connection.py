from threading import  Thread, main_thread
import socket

from src.controller import Controller
from config import env
import json

class Connection:

        users = []

        def __init__(self):   

            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
            self.server.bind(('', env('APP_PORT')))
            self.server.listen(10)
            print("Server listening...")

            self.__accept_sockets()
            

        def send(self, data):
            for user in self.users:
                user.send(data.encode('utf-8'))


        def __listening(self, client_socket):

            print("Listening user...\n")
            controller = Controller()
            while True:

                if main_thread().is_alive() is not True:
                    return 0             

                data = client_socket.recv(2048).decode('utf-8')
                if not data:
                    print(f"User {client_socket} disconnected!")
                    break
                
                data = json.loads(data)

                # Handler
                response = controller(data)
                
                # Send response
                self.send(json.dumps(response))

            client_socket.close()


        def __accept_sockets(self):

            while True:
                client_socket, client_address = self.server.accept()
                print(f'Connected by {client_address}\n')

                self.users.append(client_socket)

                listen_accepted_user = Thread(target=self.__listening, args=(client_socket,))
                listen_accepted_user.start()
