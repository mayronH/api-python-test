from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import datetime

db_connect = create_engine('sqlite:///clientes_inter.db')
app = Flask(__name__)
app.config["DEBUG"] = False
api = Api(app)

class Clientes(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM clientes")

        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)
    
    def post(self):
        conn = db_connect.connect()

        name   = request.args['name']
        age    = request.args['age']
        cpf    = request.args['cpf']
        email  = request.args['email']
        phone  = request.args['phone']
        city   = request.args['city']
        uf     = request.args['uf']
        date   = datetime.datetime.now().isoformat(" ")

        conn.execute("INSERT INTO clientes VALUES(NULL, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')"
        .format(name, age, cpf, email, phone, city, uf, date))

        query = conn.execute("SELECT * FROM clientes ORDER BY id DESC LIMIT 1")

        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self):
        conn = db_connect.connect()

        if 'id' in request.args:
            id    = request.args['id']
            name  = request.args['name']
            age   = request.args['age']
            cpf   = request.args['cpf']
            email = request.args['email']
            phone = request.args['phone']
            city  = request.args['city']
            uf    = request.args['uf']

            conn.execute("UPDATE clientes SET nome = ? , idade = ?, cpf = ?, email = ?, fone = ?, cidade = ?, uf = ? WHERE id = ?",
            (str(name), int(age), str(cpf), str(email), str(phone), str(city), str(uf), int(id)))

            query = conn.execute("SELECT * FROM clientes WHERE id=%d" % int(id))

            result =[dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            return jsonify(result)
        else:
            return "Error"

class ClienteById(Resource):
    def delete(self, id):
        conn = db_connect.connect()

        query = conn.execute("DELETE FROM clientes WHERE id=%d" % int(id))

        return {'status': 'success'}

    def get(self, id):
        conn = db_connect.connect()

        query = conn.execute("SELECT * FROM clientes where id=%d" % int(id))

        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)
        

api.add_resource(Clientes, '/clients/')
api.add_resource(ClienteById, '/clients/<id>')

if __name__ == "__main__":
    app.run()