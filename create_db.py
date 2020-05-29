import sqlite3

#Criando conexão
conn = sqlite3.connect('clientes.db')
#Fechando conexão
conn.close()