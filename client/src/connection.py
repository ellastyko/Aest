import socket
from threading import Thread

class Connection:

    __PORT__ = 9089
    __ADDR__ = 'localhost'

    def __init__(self):
        try:
            # Устанавливаем соеденение с сервером
            self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__client.connect((self.__ADDR__, self.__PORT__)) 
            listen_Theard = Thread(target=self.__listen)
            listen_Theard.start()

        except Exception as e:
            print(f'Server is not responding {e}')
    

    def __listen(self):
        while True:
            data = self.__client.recv(1024)
            print(data.decode('utf-8')) 
    

    def send(self, request):
        try: 
            self.__client.send(request.encode('utf-8')) 
        except Exception as e:
            print(f'Connection lost: {e}')


