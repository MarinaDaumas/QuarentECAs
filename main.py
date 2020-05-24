# vmo juntar as funcoes aqui
import simplejson as json
from datetime import date, time, timedelta
from banco import adicionar_pedido, buscar_clientes_contaminados, limpar_pedidos_antigos


def novo_pedido():
    """
    pedido = {"data" = data, "entregador":[nome, cpf], "cliente":[nome, email, telefone]}
    data = AAAA-MM-DD
    """
    # ler JSON no caso de cada novo pedido ser um json
    with open ("pedido.json", 'r') as ped:
        pedido = json.load(ped)

        pedido["data"] = date.today() 
    
    adicionar_pedido(pedido)

def nova_contaminacao():
    """
    aviso = {"nome": '', "cpf": ''}
    """
    #ler JSON entregador contaminado
    with open ("aviso.json", 'r') as avi:
        aviso = json.load(avi)

    expostos = buscar_clientes_contaminados(aviso[cpf])


def limpar():

    # data AAAA-MM-DD 
    hoje = date.today()
    tempo = timedelta(days=15)
    outro_dia = hoje - tempo

    limpar_pedidos_antigos(outro_dia)
    


if entrada == "pedido":
    novo_pedido()

else:
    nova_contaminacao()

limpar()