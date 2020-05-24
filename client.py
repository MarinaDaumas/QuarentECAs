import socket
import pickle
from escrever_pedido import send_json
import json

class CLIENT:
    HEADER = 10 # serve para descobrir o tamanho da mensagem, PODE SER PEQUENO
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    #SERVER = '189.5.178.202' # public ip
    SERVER = '192.168.0.11'
    ADDR = (SERVER, PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    def send(self, msg):

            message = pickle.dumps(msg)
            
            send_length = len(message)

            send_length = bytes(f"{send_length:<{self.HEADER}}", self.FORMAT)

            client.send(send_length)
            client.send(message)

    def receive(self):
        msg_length = client.recv(self.HEADER).decode(self.FORMAT) # espera a mensagem do cliente
        
        if msg_length:
            msg_length = int(msg_length)

            msg = client.recv(msg_length)
            
            msg = pickle.loads(msg)

            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            msg = json.loads(msg)

            if isinstance(msg, dict):
                print(msg["cliente"][0])
            
            print(msg)

            return msg
