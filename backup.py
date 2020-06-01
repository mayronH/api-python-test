#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3
import io

conn = sqlite3.connect('clientes.db')

#abre o arquivo clientes_dump.sql com permisão de escrita
with io.open('clientes_dump.sql', 'w') as f:
    #salva cada linha do dump do sqlite3 no arquivo aberto
    for linha in conn.iterdump():
        f.write("%s\n" % linha)

conn.close()