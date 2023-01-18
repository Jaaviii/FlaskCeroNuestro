from flask import Flask, render_template, request, redirect
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
    return render_template('index.html')

@app.route('/addvehiculo', methods=['POST'])
def addvehiculo():
    if request.method == 'POST':
        id = request.form['id']
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = request.form['ano']
        color = request.form['color']
        matricula = request.form['matricula']

        cursor = db.cursor()
        cursor.execute('INSERT INTO vehiculos (id, marca, modelo, ano, color, matricula) VALUES (%s, %s, %s, %s, %s, %s)', (id, marca, modelo, ano, color, matricula))
        db.commit()
        return render_template('index.html')

@app.route('/editar')
def editar():
    return 'editar'

@app.route('/delete')
def delete():
    return 'delete'

if __name__ == '__main__':
    app.run( debug=True)