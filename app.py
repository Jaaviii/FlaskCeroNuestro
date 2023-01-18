from flask import Flask, render_template, request, redirect, url_for
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
    cursor= mysql.connector.connect()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM vehiculos')
    data = cursor.fetchall()
    return render_template('index.html' , vehiculos = data)


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
    

@app.route('/deletevehiculos', methods=['POST'])
def delete():
    if request.method == 'POST':
        id = request.form['id']
        cursor = db.cursor()
        cursor.execute('DELETE FROM vehiculos WHERE id = %s', (id))
        db.commit()
        return render_template('index.html')
    return 'delete'

@app.route('/editar')
def editar():
    return 'editar'



if __name__ == '__main__':
    app.run( debug=True)