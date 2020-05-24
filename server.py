# criar a conexão e processar JSON
import socket
import threading
import pickle # para serializar objetos e poder mandá-los
import json
import main

class Server():
    HEADER = 10 # serve para descobrir o tamanho da mensagem, PODE SER PEQUENO
    PORT = 5050
    #SERVER = '189.5.178.202' # public ip
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"

    
    def __init__(self):
        # AF_INET = tipo da conexão, ipv4, ipv6
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR) # permite conectar nesse computador


    def handle_clients(self, conn, addr):
        print(f"[NEW CONNECTIONs] {addr} connected")
        connected = True

        while connected:
            print("esperando client1")
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT) # espera a mensagem do cliente

            if msg_length:
                msg_length_int = int(msg_length)
                msg = conn.recv(msg_length_int)
                
                if msg == self.DISCONNECT_MESSAGE:
                    connected = False
                    break

                msg = pickle.loads(msg)
                msg = json.loads(msg)
                print(msg)

            else:
                print('sem conexao')
                break

        conn.close

    def start(self): # recebe e divide os clientes
        self.server.listen()

        print(f"[LISTENING] Server is listening on {self.SERVER}")

        start_message = json.dumps("Bom DIA!")

        start_message = pickle.dumps(start_message)


        while True:
            conn, addr = self.server.accept() # espera a conexão e retorna o endereço(IP, PORT) e um objeto socket que permite mandar informações
            print("1° conectou")

            conn.send(bytes(f'{len(start_message):<{self.HEADER}}', self.FORMAT)) # transforma em bytes uma string do tipo: 'len(msg)        ' sendo do tamanho do header
            conn.send(start_message)

            thread = threading.Thread(target = self.handle_clients, args = (conn, addr))
            thread.start() 
            
            print("começou")