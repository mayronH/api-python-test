#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

id_cliente = 1
novo_nome = 'Carlos'
novo_dtcriacao = '2020-05-31'

cursor.execute("""UPDATE clientes SET nome = ?, dtcriacao = ? WHERE id = ?""",(novo_nome, novo_dtcriacao, id_cliente))

conn.commit()

conn.close()