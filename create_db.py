#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3

#Criando conexão com banco de dados
conn = sqlite3.connect('clientes.db')
#Fechando conexão
conn.close()