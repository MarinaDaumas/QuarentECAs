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

