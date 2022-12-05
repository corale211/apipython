from flask import Flask, request, jsonify 
from flask_restx import Api, Resource, reqparse
from flask_mysqldb import MySQL
#from bd import conexionbd

app = Flask(__name__)

try:
    app.config['MYSQL_HOST'] = 'mysql'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'mNmCbovvCL5QGnvb'
    app.config['MYSQL_DB'] = 'demo'    
    mysql = MySQL(app)
    cur = mysql.connection.cursor()
    print(cur)
except Exception as ex:
    print ("error")

api = Api(app)

@api.route("/consulta")
class consulta(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from Persons")
        rows = cur.fetchall()
        return jsonify(rows)

@api.route("/consulta_por_id/<string:id>")
class consulta(Resource):
    def get(self, id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from Persons where id ="+id)
        rv = cur.fetchall()
        return str(rv)
    
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return 'hello'
    
if __name__ == '__main__':
    print("Esta corriendo app.py")
    app.run(host="0.0.0.0", port=8080, debug=True)   
