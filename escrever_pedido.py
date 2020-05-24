import json
from datetime import date
import pickle


def send_msg():
    nome_c = input("seu nome, pfvor: ")
    email = input("email: ")
    telefone = input("e telefone: ")

    nome_e = "Lucio Costa"
    cpf = "167.876.352-14"

    # tratar dados
    cpf = cpf.replace('.', '')
    cpf = int(cpf.replace('-', ''))
    telefone = int(telefone)

    pedido = {"cliente":[nome_c, email, telefone], "entregador":[nome_e, cpf]}

    #pedido = pickle.dumps(pedido)

    file_name = "novo_pedido.json"

    return pedido

#print(send_json(pedido))

#with open(file_name, 'w') as outfile:
#    json.dump(pedido, outfile)





