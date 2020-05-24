# criar a conexão e processar JSON
import socket
import threading
import pickle # para serializar objetos e poder mandá-los
# pickle métodos: pickle.dump(<msg>) e pickle.loads(<msg>)
# recv() e accept() são blocks code

import json

HEADER = 10 # serve para descobrir o tamanho da mensagem, PODE SER PEQUENO
PORT = 5050
#SERVER = '189.5.178.202' # public ip
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# AF_INET = tipo da conexão, ipv4, ipv6
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) # permite conectar nesse computador

CONNECTIONS = 0


def handle_clients(conn1, addr1, conn2, addr2):
    print(f"[NEW CONNECTIONs] {addr1} e {addr2} connected")

    connected = True
    while connected:
        print("esperando client1")
        msg_length = conn1.recv(HEADER).decode(FORMAT) # espera a mensagem do cliente

        if msg_length:
            msg_length_int = int(msg_length)
            
            msg = conn1.recv(msg_length_int)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
                break

            msg_length = bytes(f"{msg_length:<{HEADER}}", FORMAT)

            conn2.send(msg_length)
            conn2.send(msg)

        msg_length = conn2.recv(HEADER).decode(FORMAT) # espera a mensagem do cliente
        print("recebi do client2")

        if msg_length:
            msg_length_int = int(msg_length)
            
            msg = conn2.recv(msg_length_int)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr1}] \n {msg}")

            msg_length_int = bytes(f"{msg_length_int:<{HEADER}}", FORMAT)

            conn1.send(msg_length_int)
            conn1.send(msg)

    conn1.close
    conn2.close

def start(): # recebe e divide os clientes
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    start_message1 = json.dumps("1")
    start_message2 = json.dumps("2")


    start_message1 = pickle.dumps(start_message1)
    start_message2 = pickle.dumps(start_message2)
        

    while True:
        conn1, addr1 = server.accept() # espera a conexão e retorna o endereço(IP, PORT) e um objeto socket que permite mandar informações
        print("1° conectou")
        
        conn1.send(bytes(f'{len(start_message1):<{HEADER}}', FORMAT)) # transforma em bytes uma string do tipo: 'len(msg)        ' sendo do tamanho do header
        conn1.send(start_message1)
        
        conn2, addr2 = server.accept() # espera a conexão e retorna o endereço(IP, PORT) e um objeto socket que permite mandar informações



        conn2.send(bytes(f'{len(start_message2):<{HEADER}}', FORMAT))
        conn2.send(start_message2)
        print("2° conectou")


        thread = threading.Thread(target = handle_clients, args = (conn1, addr1, conn2, addr2))
        thread.start() 
        print("começou")


print("[STARTING] server is starting")
start()