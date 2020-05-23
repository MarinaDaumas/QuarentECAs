# guardar entregador(cpf), email, nome do cliente, data, status
# mandar emails 
  
import sqlite3

id = 1
CPF_c = 123
CPF_e = 321
nome_e = "evanilson"
nome_c = "jorge"
email_c = "kkk"
data = 22
cliente = 2
telefone = 99999999

conn = sqlite3.connect('covid.db')
cursor = conn.cursor()
####
cursor.execute("""
CREATE TABLE IF NOT EXISTS entregador (
        cpf INTEGER PRIMARY KEY,
        nome TEXT
);
""")

cursor.execute("""
INSERT INTO entregador (cpf,nome)
VALUES (?,?)
""", (CPF_e, nome_e))
conn.commit()
#
####
cursor.execute("""
CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefone
);
""")

cursor.execute("""
INSERT INTO cliente (nome,email,telefone)
VALUES (?,?,?)
""", (nome_c,email_c,telefone))
conn.commit()
#
#####
cursor.execute("""
CREATE TABLE IF NOT EXISTS entregas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        data INTEGER,
        cpf_entregador INTEGER,
        email_cliente TEXT
);
""")

cursor.execute("""
INSERT INTO entregas (data)
VALUES (?)
""", (data,cpf_e,email_c))
conn.commit()



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
    id_cliente = checar_cliente(pedido[cliente]) 
    id_entregador = checar_entregador(pedido[entregador])   

    


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
    Output: clientes = lista com todos os clientes expostos 
    """
    pass
