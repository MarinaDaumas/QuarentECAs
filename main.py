# vmo juntar as funcoes aqui
import simplejson as json
from banco import adicionar_pedido, buscar_clientes_contaminados


def novo_pedido():

    # ler JSON no caso de cada novo pedido ser um json
    with open ("pedido.json", 'r') as ped:
        pedido = json.load(ped)

    adicionar_pedido(pedido)

def nova_contaminacao():

    #ler JSON entregador contaminado
    with open ("aviso.json", 'r') as avi:
        aviso = json.load(avi)





if entrada == "pedido":
    novo_pedido()

else:
    nova_contaminacao()
