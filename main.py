# vmo juntar as funcoes aqui
import json
from datetime import date, timedelta
from banco import adicionar_pedido, buscar_clientes_contaminados, limpar_pedidos_antigos


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

    expostos = buscar_clientes_contaminados(aviso[cpf])

    for dados_entrega in expostos:
        mandar_email(dados_entrega)


def limpar():
    # data AAAA-MM-DD 
    hoje = date.today()
    tempo = timedelta(days=15)
    outro_dia = hoje - tempo

    limpar_pedidos_antigos(outro_dia)
    
# {"cliente":[nome_c, email, telefone], "entregador":[nome_e, cpf]}

def main(msg):
    limpar()
    print("type: ", type(msg), " and msg: ", msg)
    if msg.get("cliente", 0):
        novo_pedido(msg)
    else:
        nova_contaminacao(msg)


# if entrada == "pedido":
#     novo_pedido()

# else:
#     nova_contaminacao()

    #nova_contaminacao()