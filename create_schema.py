#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3

conn = sqlite3.connect('clientes.db')

#criando um cursor = Algo como um pointer para navegação no banco de dados
cursor = conn.cursor()

#Criando tabelas
#Execute = executa as instruções no banco de dados
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