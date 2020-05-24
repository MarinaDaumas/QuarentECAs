import socket
import pickle
from escrever_pedido import send_msg
from escrever_aviso import send_aviso
import json

class CLIENTE:
    HEADER = 10 # serve para descobrir o tamanho da mensagem, PODE SER PEQUENO
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    #SERVER = '189.5.178.202' # public ip
    SERVER = '127.0.1.1'
    ADDR = (SERVER, PORT)


    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        self.receive()

    def send(self, msg):
        msg = json.dumps(msg)
        message = pickle.dumps(msg)
        send_length = len(message)
        send_length = bytes(f"{send_length:<{self.HEADER}}", self.FORMAT)
        self.client.send(send_length)
        self.client.send(message)

    def receive(self):
        msg_length = self.client.recv(self.HEADER).decode(self.FORMAT) # espera a mensagem do cliente
        
        if msg_length:
            msg_length = int(msg_length)
            msg = self.client.recv(msg_length)
            msg = pickle.loads(msg)

            if msg == self.DISCONNECT_MESSAGE:
                connected = False
            
            msg = json.loads(msg)

            if isinstance(msg, dict):
                print(msg["cliente"][0])
            
            print(msg)
            return msg


client = CLIENTE()
client.send(send_aviso())