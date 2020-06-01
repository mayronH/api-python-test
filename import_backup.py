#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3
import io

conn = sqlite3.connect('clientes_new.db')

cursor = conn.cursor()

#abre o arquivo com permissão de leitura
f = io.open('clientes_dump.sql', 'r')
sql =  f.read()
#executa o script sql
cursor.executescript(sql)

conn.close()