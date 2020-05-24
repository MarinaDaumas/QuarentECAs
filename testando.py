from banco import *
import datetime 
'''
def limpar():

    # data AAAA-MM-DD 
    hoje = date.today()
    tempo = timedelta(days=15)
    outro_dia = hoje - tempo

    limpar_pedidos_antigos(outro_dia)
'''
if __name__ == "__main__":
    criar_tabelas()
    
    hora = datetime.date.today()
    pedido = {"data" : hora, "entregador":['robson', 8520741], "cliente":['CLodoaldo Silva', 'clo.clo@gmail.com', 40028922]}
    adicionar_pedido(pedido)
    
    #buscar_clientes_contaminados(175855)
    #limpar()
