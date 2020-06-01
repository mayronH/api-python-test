#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

cursor.execute("""ALTER TABLE clientes ADD COLUMN ativo BOOLEAN""")

conn.commit()

conn.close()