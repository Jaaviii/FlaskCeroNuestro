from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from data.vehiculos_dao import VehiculoDao
from data.modelo.vehiculo import Vehiculo
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
   
    

@app.route('/vehiculos.html')
def vehiculos():
    
    vehiculo_dao : VehiculoDao = VehiculoDao(db)
   
    return render_template('vehiculos.html' , vehiculos = vehiculo_dao.dameTodosLosVehiculos())


@app.route('/multas.html')
def multas():   
    return render_template('multas.html')


@app.route('/addvehiculo', methods=['POST'])
def addvehiculo():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = request.form['ano']
        color = request.form['color']
        matricula = request.form['matricula']

        vehiculo = Vehiculo(marca, modelo, ano, color, matricula)
        vehiculo_dao : VehiculoDao = VehiculoDao(db)
        vehiculo_dao.addvehiculo(vehiculo)
        return redirect(url_for('vehiculos'))
    

@app.route('/deletevehiculo/<string:id>')
def deletevehiculo(id):
    #cursor = db.cursor()
    #cursor.execute('DELETE FROM vehiculos WHERE id = {0}'.format(id))
    #db.commit()
    vehiculo_dao : VehiculoDao = VehiculoDao(db)
    vehiculo_dao.deletevehiculo(id)
    return redirect(url_for('vehiculos'))



if __name__ == '__main__':
    app.run( debug=True)