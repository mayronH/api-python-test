#Baseado em: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte2.html
import sqlite3

class Connect(object):

    def __init__(self, db_name):
        super().__init__()
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()

            #Pega a versão do sqlite
            self.cursor.execute("SELECT SQLITE_VERSION()")
            self.data = self.cursor.fetchone()
        except sqlite3.Error:
            print("Erro ao conectar com o banco")
    
    def close_db(self):
        if self.conn:
            self.conn.close()

class ClienteDB(object):

    def __init__(self):
        self.db = Connect('clientes_inter.db')

    def close_connection(self):
        self.db.close_db()

if __name__ == '__main__':
    cliente = ClienteDB()
    cliente.close_connection()