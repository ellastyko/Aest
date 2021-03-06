import socket
from threading import Thread, main_thread, enumerate
import json 

class Connection:

    __PORT__ = 9090
    __ADDR__ = 'localhost'

    def __init__(self):
        try:
            # Устанавливаем соеденение с сервером
            self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__client.connect((self.__ADDR__, self.__PORT__)) 
            listen_theard = Thread(target=self.__listen)
            listen_theard.start()
            
        except Exception as e:
            print(f'Server is not responding {e}')
    

    def __listen(self):
        while True:
            if main_thread().is_alive() is not True:
                return 0
            data = self.__client.recv(1024)
            print(data.decode('utf-8')) 
    

    def send(self, request):
        try: 
            self.__client.send(json.dumps(request).encode('utf-8')) 
        except Exception as e:
            print(f'Connection lost: {e}')
    
    def threads(self):
        return enumerate()


