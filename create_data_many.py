#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

lista = [('Mateus', 20, '11122233389', 'mateus@teste.com.br', '31955554444', 'Timóteo', 'MG', '2020-05-30'),
        ('Ana', 18, '15155544478', 'ana@teste.com.br', '31955554489', 'Coronel Fabriciano', 'MG', '2020-05-29'),
        ('Luiza', 25, '22233355566', 'luiza@teste.com.br', '31944554489', 'Ipatinga', 'MG', '2020-06-02'),
        ('Pedro', 30, '11188899900', 'pedro@teste.com.br', '31944558889', 'São Paulo', 'SP', '2020-06-02')]

#Insere várias entradas no banco
cursor.executemany("""INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, dtcriacao)
                    VALUES(?,?,?,?,?,?,?,?)""", lista)

conn.commit()

conn.close()