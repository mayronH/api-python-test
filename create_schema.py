import sqlite3

conn = sqlite3.connect('clientes.db')

#criando um cursor
cursor = conn.cursor()

#Criando tabelas

cursor.execute("""CREATE TABLE clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL,
    email TEXT NOT NULL,
    fone TEXT,
    cidade TEXT,
    uf VARCHAR(2) NOT NULL,
    dtcriacao DATE NOT NULL
);""")

conn.close()