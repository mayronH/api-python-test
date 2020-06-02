#Baseado em: https://medium.com/@nataniel.paiva/cria%C3%A7%C3%A3o-de-uma-api-rest-com-python-76696d17bfb9
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


db_connect = create_engine('sqlite:///exemplo.db')
app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM user")
        
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        
        name = request.json['name']
        email = request.json['email']

        conn.execute("INSERT INTO user VALUES(NULL, '{0}', '{1}')".format(name, email))

        query = conn.execute("SELECT * FROM user ORDER BY id DESC LIMIT 1")

        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self):
        conn = db_connect.connect()
        id = request.json['id']
        name = request.json['name']
        email = request.json['email']

        conn.execute("UPDATE user SET name='" + str(name) + "', email='" + str(email) + "' WHERE id=%d" % int(id))

        query = conn.execute("SELECT * FROM user WHERE id=%d" % int(id))

        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

class UserById(Resource):
    def delete(self, id):
        conn = db_connect.connect()
        conn.execute("DELETE FROM user WHERE id=%d" % int(id))

        return {'status': 'success'}

    def get(self, id):
        conn = db_connect.connect()

        query = conn.execute("SELECT * FROM user WHERE id=%d" % int(id))

        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<id>')

if __name__ == '__main__' :
    app.run()