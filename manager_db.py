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
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print("Error: A tabela %s já existe" % self.tb_name)
            return False

if __name__ == '__main__':
    c = ClienteDB()
    c.criar_schema()