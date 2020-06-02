import os
import sqlite3
import io
import datetime
import names
import csv
from gen_random_values import *
from connect_db import *

class ClienteDB(ClienteDB):

    def criar_schema(self, schema_name='sql/clientes_schema.sql'):

        try:
           # Abre arquivo para leitura no modo texto
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)

        except sqlite3.Error:
            print("Error: A tabela %s já existe" % self.tb_name)
            return False

    def inserir_registro(self):
        try:
            self.db.cursor.execute("""INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, dtcriacao) 
            VALUES ('Mayron', 23, '12345678901', 'teste@gmail.com', '(31)97777-6666', 'Timóteo', 'MG', '2020-06-02 09:14:00.199000')""")
            
            self.db.commit_db()

        except sqlite3.IntegrityError:
            print('Erro ao inserir novo registro. O CPF e email devem ser únicos.')
            return False

    def inserir_com_lista(self):
        lista = [('Julia', 18, '55566677789', 'julia@teste.com.br', '(31)98585-6363', 'Coronel Fabriciano', 'MG', '2020-06-01 09:20:00.199000'),
                 ('Pedro', 30, '88877766655', 'pedro@teste.com.br', '(31)92233-4455', 'Ipatinga', 'MG', '2020-06-03 09:30:00.199000'),
                 ('Maria', 25, '66644499912', 'maria@teste.com.br', '(31)94567-1234', 'Timóteo', 'MG', '2020-06-03 09:25:00.199000'),
                 ('José', 22, '45678912396', 'jose@teste.com.br', '(31)97788-5522', 'Belo Horizonte', 'MG', '2020-05-31 12:25:00.199000')]
        
        try:
            self.db.cursor.executemany("""INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, dtcriacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", lista)

            self.db.commit_db()
        except sqlite3.IntegrityError:
            print("Erro ao inserir novo registro. O CPF e email devem ser únicos.")
            return False

    def inserir_de_arquivo(self):
        try:
            with open('sql/clientes_dados.sql', 'rt') as f:
                dados = f.read()
                self.db.cursor.executescript(dados)

                self.db.commit_db()
        except sqlite3.IntegrityError:
            print("Erro ao inserir novo registro. O CPF e email devem ser únicos.")
            return False

    def inserir_de_csv(self, file_name='csv/clientes.csv'):
        try:
            # Delimiter = separa os campos com virgula
            reader = csv.reader(
                open(file_name, 'rt'), delimiter=','    
            )
            linha = (reader,)
            for linha in reader:
                self.db.cursor.execute("""INSERIR INTO clientes (nome, idade, cpf, email, fone, cidade, uf, dtcriacao)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", linha)
            
            self.db.commit_db()
        except sqlite3.IntegrityError:
            print("Erro ao inserir novo registro. O CPF e email devem ser únicos.")
            return False
    
    def inserir_random(self, repeat=5):
        # Cria uma lista vazia
        lista = []

        for i in range(repeat):
            # Cria uma data com o horário atual, isoformat retira o caracter 'T' gerado pela função
            date = datetime.datetime.now().isoformat(" ")
            fname = names.get_first_name()
            lname = names.get_last_name()
            # Concatena o primeiro com o segundo nome
            name = fname + " " + lname
            # Cria um email com a primeira letra do primeiro nome . segundo nome @gmail.com
            email = fname[0].lower() + '.' + lname.lower() + '@gmail.com'
            c = gen_city()
            city = c[0]
            uf = c[1]

            lista.append(name, gen_age(), gen_cpf(), email, gen_phone(), city, uf, date)

        try:
            self.db.cursor.executemany("""INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, dtcriacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", lista)

            self.db.commit_db()
        except sqlite3.IntegrityError:
            print("Erro ao inserir novo registro. O CPF e email devem ser únicos.")
            return False

    def read_all_clients(self):
        sql = "SELECT * FROM clientes ORDER BY id"
        r = self.db.cursor.execute(sql)
        return r.fetchall()

    def print_all_clients(self):
        lista = self.read_all_clients()
        # Formata em formato tabela
        # Cada {} é uma celula
        # : começa a regra da formatação
        # > alinhamento a direita, < alinhamento a esquerda
        # O número indica o espaço de caracteres
        # s indica tipo string
        print('{:>3s} {:20s} {:<5s} {:15s} {:21s} {:14s} {:15s} {:s} {:s}'.format(
            'id', 'nome', 'idade', 'cpf', 'email', 'fone', 'cidade', 'uf', 'dtcriacao'
        ))
        for cliente in lista:
            print('{:>3d} {:23s} {:<2d} {:s} {:>25s} {:s} {:15s} {:s} {:s}'.format(
                cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6], cliente[7], cliente[8]
            ))

    def search_client(self, id):
        r = self.db.cursor.execute(
            'SELECT * FROM clientes WHERE id= ?', (id,))
        return r.fetchone()

    def print_client(self, id):
        if self.search_client(id) == None:
            print("Não foi encontrado um cliente com esse ID")
        else:
            cliente = self.search_client(id)
            print('{:>3s} {:20s} {:<5s} {:15s} {:21s} {:14s} {:15s} {:s} {:s}'.format(
            'id', 'nome', 'idade', 'cpf', 'email', 'fone', 'cidade', 'uf', 'dtcriacao'
            ))
            print('{:>3d} {:23s} {:<2d} {:s} {:>25s} {:s} {:15s} {:s} {:s}'.format(
                cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], 
                cliente[5], cliente[6], cliente[7], cliente[8]
            ))

    def update_client(self, id):
        try:
            cliente = self.search_client(id)

            if cliente:
                self.novo_fone = input('Fone: ')
                self.db.cursor.execute("""UPDATE clientes SET fone = ? WHERE id = ?""", (self.novo_fone, id, ))

                self.db.commit_db()

            else:
                print("Nenhum cliente encontrado")
        except sqlite3.IntegrityError:
            print("Erro ao inserir novo registro. O CPF e email devem ser únicos.")
            return False

    def deletar(self, id):
        try:
            cliente = self.search_client(id)

            if cliente:
                self.db.cursor.execute("""DELETE FROM clientes WHERE id = ?""", (id,))

                self.db.commit_db()

            else:
                print("Nenhum cliente encontrado")
        except sqlite3.IntegrityError:
            print("Erro ao inserir novo registro. O CPF e email devem ser únicos.")
            return False

class PessoaDB(object):
    tb_name = 'pessoas'

    def __init__(self):
        self.db = Connect('pessoas.db')
        self.tb_name

    def criar_schema(self, schema_name='sql/pessoas_schema.sql'):
        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print("Error: A tabela %s já existe" % self.tb_name)
            return False

    def inserir_csv(self, file_name='csv/cidades.csv'):
        try:
            reader = csv.reader(
                open(file_name, 'rt'), delimiter=',')

            linha = (reader,)
            for linha in reader:
                self.db.cursor.execute("""INSERT INTO cidades (cidade, uf) VALUES (?, ?)""", linha)
            
            self.db.commit_db()

        except sqlite3.IntegrityError:
            print('Erro ao inserir cidades')
            return False
    
    def gen_cidade(self):
        sql = "SELECT COUNT(*) FROM cidades"
        query = self.db.cursor.execute(sql)
        return query.fetchone()[0]

    def inserir_random(self, repeat=5):
        lista = []

        for i in range(repeat):
            fname = names.get_first_name()
            lname = names.get_last_name()
            email = fname[0].lower() + "." + lname.lower() + "@gmail.com"
            idcidade = random.randint(1, self.gen_cidade())
            lista.append((fname, lname, email, idcidade))

        try:
            self.db.cursor.executemany("""INSERT INTO pessoas(nome, sobrenome, email, idcidade) 
                VALUES (?, ?, ?, ?)""", lista)
            
            self.db.commit_db()

        except sqlite3.IntegrityError:
            print('Erro ao inserir dados')
            return False

    def read_all(self):
        sql = "SELECT * FROM pessoas INNER JOIN cidades ON pessoas.idcidade = cidades.id"
        query = self.db.cursor.execute(sql)
        return query.fetchall()

    def print_all(self):
        lista = self.read_all()
        # for p in lista:
        #     print(p)
        print('{:>3s} {:15s} {:15s} {:>21s} {:15s} {:s}'.format(
            'id', 'nome', 'sobrenome', 'email', 'cidade', 'dtcriacao'
        ))
        for pessoa in lista:
            print('{:>3d} {:15s} {:15s} {:>21s} {:15s} {:s}'.format(
                pessoa[0], pessoa[1], pessoa[2], pessoa[3], pessoa[7], pessoa[5]
            ))
        
    def table_list(self):
        lista = self.db.cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")
        print("Tabelas: ")
        for tabela in lista.fetchall():
            # print("{}".format(tabela))
            print("%s" % (tabela))

    def fechar_conexao(self):
        self.db.close_db()

if __name__ == '__main__':
    # c = ClienteDB()
    # c.criar_schema()
    # # c.inserir_registro()
    # # c.inserir_com_lista()
    # # c.inserir_de_arquivo()
    # c.deletar(11)
    # c.print_all_clients()
    p = PessoaDB()
    # p.criar_schema()
    # p.inserir_csv()
    # p.inserir_random()
    p.print_all()
    p.table_list()