#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

table_name = 'clientes'

cursor.execute('PRAGMA table_info({})'.format(table_name))

print('Colunas:')
colunas = [tupla[1] for tupla in cursor.fetchall()]
for coluna in colunas:
    print(coluna)

cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")

print('Tabelas:')
for tabela in cursor.fetchall():
    print("%s" % (tabela))

cursor.execute("""SELECT sql FROM sqlite_master WHERE type='table' AND name=?""", (table_name,))

print('Schema:')
for schema in cursor.fetchall():
    print("%s" % (schema))

conn.close()