import json
from datetime import date
import pickle


def send_msg():
    nome_c = "heitor"
    email = "heitor_ndrd@poli.ufrj.br"
    telefone = "985598983"

    nome_e = "Lucio Costa"
    cpf = "167.876.352-14"

    # tratar dados
    cpf = cpf.replace('.', '')
    cpf = int(cpf.replace('-', ''))
    telefone = int(telefone)

    pedido = {"cliente":[nome_c, email, telefone], "entregador":[nome_e, cpf]}

    file_name = "novo_pedido.json"

    return pedido






