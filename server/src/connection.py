import socket
import threading

class Connection():

        users = []
        __PORT__ = 9089

        def __init__(self):
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
            self.server.bind(('', self.__PORT__))
            self.server.listen(10)
            
            print("Server listening...")
            self.__accept_sockets()
            

        def send(self, data):
            for user in self.users:
                user.send(data.encode('utf-8'))


        def __listening(self, client_socket):

            print("Listening user...\n")
            # print(threading.current_thread())
            # print(threading.active_count()) 
            # print(threading.enumerate())

            while True:
                
                data = client_socket.recv(1024)
                data = data.decode('utf-8')
                self.send(data)


        def __accept_sockets(self):

            while True:
                client_socket, client_address = self.server.accept()
                print('Connected by', client_address)

                self.users.append(client_socket)

                listen_accepted_user = threading.Thread(target=self.__listening, args=(client_socket,))
                listen_accepted_user.start()