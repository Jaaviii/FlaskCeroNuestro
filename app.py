from flask import Flask
from flask_mysqldb import MySQL
import mysql.connector
app = Flask(__name__)

db = mysql.connector.connect(
    host ='informatica.iesquevedo.es',
    port = 3333,
    user ='root',
    password ='1asir', 
    database='elduo'
) 

@app.route('/')
def Index():
    return 'hola mundo'

@app.route('/addvehiculo')
def vehiculo():
    return 'add vehiculo'

@app.route('/editar')
def editar():
    return 'editar'

@app.route('/delete')
def delete():
    return 'delete'

if __name__ == '__main__':
    app.run( debug=True)