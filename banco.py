# guardar entregador(cpf), email, nome do cliente, data, status
# mandar emails 
  
import sqlite3

avisos = []
l_dados = []

from datetime import datetime

data = datetime.today().strftime('%Y-%m-%d')


id = 1
CPF_c = 123
CPF_e = 3214
nome_e = "evanilson"
nome_c = "jorge"
email_c = "kkk"
data = 22
cliente = 2
telefone = 99999999

conn = sqlite3.connect('covid.db')
cursor = conn.cursor()


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
        email_cliente TEXT
);
""")



def checar_cliente(cliente):
    """
    Procura cliente no banco de dados. Caso o cliente ja esteja cadastrado nada acontece.
    Input: entregador = dicionario com todos os dados do cliente
    Output: id_cliente
    """
    email = cursor.execute("""
    SELECT nome
    FROM clientes
    WHERE cpf=(?);
    """,(cliente[1],)).fetchall()

    if email == []:
        id_cliente = adicionar_clientes(cliente)
        return id_cliente
    else:
        return email
        

def checar_entregador(entregador):
    """
    Procura entregador no banco de dados. Caso o entregador ja esteja cadastrado nada acontece.
    Input: entregador = dicionario com todos os dados do entregador
    Output: id_entregador
    """
    x = entregador[1]
    cpf = cursor.execute("""
    SELECT cpf
    FROM entregadores
    WHERE cpf=(?);
    """,(x,)).fetchall()

    if cpf == []:
        id_entregador = adicionar_entregador(entregador)
        return id_entregador
    else:
        return cpf 
        

def adicionar_clientes(cliente):
    """
    Adiciona cadastro do novo cliente ao banco.
    """
    x = cliente[0]
    y = cliente[1]
    z = cliente[2]

    cursor.execute("""
    INSERT INTO cliente (nome,email,telefone)
    VALUES (?,?,?)
    """, (x,y,z))
    conn.commit()
    return x


def adicionar_entregador(entregador):
    """
    Adiciona cadastro do novo entregador ao banco.
    """
    cursor.execute("""
    INSERT INTO entregador (cpf,nome)
    VALUES (?,?)
    """, (entregador[1], entregador[0]))
    conn.commit()
    return entregador[1]


def adicionar_pedido(pedido):
    """
    Adiciona dados do novo pedido.
    """
    id_cliente = checar_cliente(pedido[cliente]) 
    id_entregador = checar_entregador(pedido[entregador])   

    cursor.execute("""
    INSERT INTO entregas (data)
    VALUES (?)
    """, (pedido,id_entregador,id_cliente))
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
    SELECT data
    FROM entregas
    WHERE cpf_entregador=(?);
    """,(cpf_entregador,)).fetchall()
    conn.commit()

    l_email = cursor.execute("""
    SELECT email_cliente
    FROM entregas
    WHERE cpf_entregador=(?);
    """,(cpf_entregador,)).fetchall()
    conn.commit()

    x = len(l_email)
    for i in range(x):
        print(i)
        k = l_email[i]
        
        x = cursor.execute("""
        SELECT *
        FROM clientes
        WHERE email=(?);
        """,(k)).fetchall()

        l_dados.append(x[i])
        
    print(l_dados)
    for i in range(len(l_email)):
        avisos.append([l_data[i][0],l_dados[i][1],l_dados[i][2]])




    print(avisos)
