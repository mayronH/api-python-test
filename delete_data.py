#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

id_cliente = 8

cursor.execute("""DELETE FROM clientes WHERE id = ?""", (id_cliente,))

conn.commit()

conn.close()