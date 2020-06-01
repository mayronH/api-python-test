#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

cursor.execute(""" INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, dtcriacao ) 
                    VALUES ('Teste1', 23, '00123456789', 'teste@teste.com.br', '31998980101', 'Timóteo', 'MG', '2020-06-01')""")

cursor.execute(""" INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, dtcriacao ) 
                    VALUES ('Teste2', 18, '98765432100', 'teste2@teste.com.br', '31998980101', 'Coronel Fabriciano', 'MG', '2020-06-01')""")

cursor.execute(""" INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, dtcriacao ) 
                    VALUES ('Teste3', 17, '12345678900', 'teste3@teste.com.br', '31998980101', 'Ipatinga', 'MG', '2020-06-02')""")

cursor.execute(""" INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, dtcriacao ) 
                    VALUES ('Teste4', 25, '11122233344', 'teste4@teste.com.br', '31998980101', 'Timóteo', 'MG', '2020-06-03')""")

#Gravar no banco de dados
conn.commit()

conn.close()