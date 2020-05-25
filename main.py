# vmo juntar as funcoes aqui
# -*- coding: utf-8 -*-
import json
from datetime import date, timedelta
from banco import adicionar_pedido, buscar_clientes_contaminados, limpar_pedidos_antigos
from mensagem import mandar_email

def convert(string): 
    li = list(string.split("-")) 
    x = li.reverse()
    k = '/'.join(li)
    return k

def novo_pedido(pedido):
    """
    pedido = {"entregador":[nome, cpf], "cliente":[nome, email, telefone]}
    data = AAAA-MM-DD
    """

    pedido["data"] = date.today()
    print(pedido)
    adicionar_pedido(pedido)

def nova_contaminacao(aviso):
    """
    aviso = {"nome": '', "cpf": ''}
    expostos = lista de dic 
    """
    #ler JSON entregador contaminado
    print("em nova contaminação: ")
    print(aviso["cpf"])

    expostos = buscar_clientes_contaminados(aviso["cpf"])
    
    for entrega in expostos:
        x = []
        x = entrega['data']
        y = convert(x)   
        entrega['data'] = y

        print("no primeiro for", entrega["email"])
        mandar_email(entrega["nome"], entrega["email"], entrega["data"])

    #for dados_entrega in expostos:
    #    mandar_email(dados_entrega)


def limpar():
    # data AAAA-MM-DD 
    hoje = date.today()
    tempo = timedelta(days=4)
    outro_dia = hoje - tempo

    limpar_pedidos_antigos(outro_dia)
    
# {"cliente":[nome_c, email, telefone], "entregador":[nome_e, cpf]}

def main(msg):
    limpar()
    print("type: ", type(msg), " and msg: ", msg)
    if msg.get("cliente", 0):
        print('no if da main \n\n\n')
        novo_pedido(msg)
    else:
        print('no else da main \n\n\n')
        nova_contaminacao(msg)


# if entrada == "pedido":
#     novo_pedido()

# else:
#     nova_contaminacao()

    #nova_contaminacao()