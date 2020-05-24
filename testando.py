from banco import *
from datetime import date, time, timedelta

def limpar():

    # data AAAA-MM-DD 
    hoje = date.today()
    tempo = timedelta(days=-1)
    outro_dia = hoje - tempo

    limpar_pedidos_antigos(outro_dia)

if __name__ == "__main__":
    criar_tabelas()
    '''
    hora = datetime.today()
    pedido = {"data" : hora, "entregador":['robson', 175855], "cliente":['jose', 'ze@gmail.com', 3654]}
    adicionar_pedido(pedido)
    '''
    #buscar_clientes_contaminados(175855)
    #limpar()
