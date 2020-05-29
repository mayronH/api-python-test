import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

cursor.execute(""" INSERT INTO clientes(nome, idade, cpf, email, ) """)