#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

cursor.execute("""SELECT * FROM clientes;""")

for i in cursor.fetchall():
    print(i)

conn.close()