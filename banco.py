# guardar entregador(cpf), email, nome do cliente, data, status
# mandar emails 
  
import sqlite3
from datetime import date

avisos = []
l_dados = []



conn = sqlite3.connect('covid.db')
cursor = conn.cursor()

def criar_tabelas():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entregadores (
            cpf INTEGER PRIMARY KEY,
            nome TEXT
    );
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone INTEGER
    );
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entregas (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            data DATE,
            cpf_entregador INTEGER,
            id_cliente INTEGER
    );
    """)



def checar_cliente(cliente):
    """
    Procura cliente no banco de dados. Caso o cliente ja esteja cadastrado nada acontece.
    Input: entregador = dicionario com todos os dados do cliente
    Output: id_cliente
    """

    # Por enquanto apenas clientes cadastrados com email. Adaptar para telefone mais tarde
    
    email = cliente[1] 

    id_cliente = cursor.execute("""
    SELECT id
    FROM clientes
    WHERE email=(?);
    """,(email,)).fetchall()

    if id_cliente == []:
        id_cliente = adicionar_clientes(cliente)
    
    return id_cliente
        

def checar_entregador(entregador):
    """
    Procura entregador no banco de dados. Caso o entregador ja esteja cadastrado nada acontece.
    Input: entregador = dicionario com todos os dados do entregador
    Output: id_entregador
    """
    cpf = entregador[1]

    cpf = cursor.execute("""
    SELECT cpf
    FROM entregadores
    WHERE cpf=(?);
    """,(cpf,)).fetchall()

    if cpf == []:
        cpf = adicionar_entregador(entregador)

    return cpf 
        

def adicionar_clientes(cliente):
    """
    Adiciona cadastro do novo cliente ao banco.
    """
    nome = cliente[0]
    email = cliente[1]
    telefone = cliente[2]

    cursor.execute("""
    INSERT INTO clientes (nome,email,telefone)
    VALUES (?,?,?)
    """, (nome, email, telefone))
    conn.commit()

    id_cliente = cursor.execute("""
    SELECT id
    FROM clientes
    WHERE nome=(?);
    """,(nome,)).fetchall()

    return id_cliente


def adicionar_entregador(entregador):
    """
    Adiciona cadastro do novo entregador ao banco.
    """

    cpf = entregador[1]
    nome = entregador[0]

    cursor.execute("""
    INSERT INTO entregadores (cpf,nome)
    VALUES (?,?)
    """, (cpf, nome))
    conn.commit()

    return cpf


def adicionar_pedido(pedido):
    """
    Adiciona dados do novo pedido.
    """
    id_cliente = checar_cliente(pedido['cliente']) 
    id_entregador = checar_entregador(pedido['entregador'])   

    id_cliente = id_cliente[0][0]
    id_entregador = id_entregador[0][0]
    data = pedido['data']

    cursor.execute("""
    INSERT INTO entregas (data, cpf_entregador, id_cliente)
    VALUES (?, ?, ?)
    """, (data, id_entregador[0][0], id_cliente[0][0]))
    conn.commit()

    


def limpar_pedidos_antigos(data):
    """
    Apaga do banco registros de pedidos feitos a mais de 15.
    Input: data = data mais antiga a nao ser apagada
    """
    
    cursor.execute("""
    DELETE FROM entregas
    WHERE data<=(?);
    """,(data,))
    conn.commit()


def buscar_clientes_contaminados(cpf_entregador):
    """
    Busca dados de clientes expostos a entregadores possivelmente contaminados.
    Input: id_entregador
    Output: clientes = lista com todos os clientes expostos 
    """

    l_data = cursor.execute("""
    SELECT data, id_cliente
    FROM entregas
    WHERE cpf_entregador=(?);
    """,(cpf_entregador,)).fetchall()
    conn.commit()
   
    avisos = []

    for i in range(len(l_data)):
        #print(i)
        data = l_data[i][0]
        id_cliente = l_data[i][1]
        
        dados_cliente = cursor.execute("""
        SELECT nome, email, telefone
        FROM clientes
        WHERE id=(?);
        """,(id_cliente,)).fetchall()

           
        avisos.append({"data":data, "nome":dados_cliente[0][0], "email":dados_cliente[0][1], "telefone":dados_cliente[0][2]})

    #print(avisos)
    return avisos

