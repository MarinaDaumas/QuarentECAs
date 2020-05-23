# guardar entregador(cpf), email, nome do cliente, data, status
# mandar emails 




def checar_cliente(cliente):
    """
    Procura cliente no banco de dados. Caso o cliente ja esteja cadastrado nada acontece.
    Input: entregador = dicionario com todos os dados do cliente
    Output: id_cliente
    """
    if nao_cadastrado:
        id_cliente = adicionar_clientes(cliente)

    return id_cliente
        

def checar_entregador(entregador):
    """
    Procura entregador no banco de dados. Caso o entregador ja esteja cadastrado nada acontece.
    Input: entregador = dicionario com todos os dados do entregador
    Output: id_entregador
    """
    if nao_cadastrado:
        id_entregador = adicionar_entregador(entregador)

    return id_entregador
        

def adicionar_clientes(cliente):
    """
    Adiciona cadastro do novo cliente ao banco.
    """
    return id_cliente


def adicionar_entregador(entregador):
    """
    Adiciona cadastro do novo entregador ao banco.
    """
    return id_entregador


def adicionar_pedido(pedido):
    """
    Adiciona dados do novo pedido.
    """
    pass


def limpar_pedidos_antigos(data):
    """
    Apaga do banco registros de pedidos feitos a mais de 15.
    Input: data = dia de hoje
    """
    pass


def buscar_clientes_contaminados(cpf_entregador):
    """
    Busca dados de clientes expostos a entregadores possivelmente contaminados.
    Input: id_entregador
    Output: clientes = lista de dicionarios com todos os clientes expostos 
    """
    pass