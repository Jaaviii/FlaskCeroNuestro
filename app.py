from flask import Flask, render_template, request, redirect, url_for
from data.vehiculos_dao import VehiculoDao
from data.modelo.vehiculo import Vehiculo
from data.modelo.multas import Multa
from data.multas_dao import MultaDao
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
    vehiculo_dao : VehiculoDao = VehiculoDao(db)
    vehiculo_dao.deletevehiculo(id)
    return redirect(url_for('vehiculos'))

@app.route('/multas.html')
def multas():   

    multa_dao : MultaDao = MultaDao(db)
    return render_template('multas.html', multas = multa_dao.dameTodasLasMultas())

    

@app.route('/addmulta', methods=['POST'])
def addmulta():
    if request.method == 'POST':
        fecha = request.form['fecha']
        lugar = request.form['lugar']
        descripcion = request.form['descripcion']
        id_vehiculo = request.form['id_vehiculo']

        multa = Multa(fecha, lugar, descripcion, id_vehiculo)
        multa_dao : MultaDao = MultaDao(db)
        multa_dao.addmulta(multa)
        return redirect(url_for('multas'))

@app.route('/deletemulta/<string:id>')
def deletemulta(id):
    multa_dao : MultaDao = MultaDao(db)
    multa_dao.deletemulta(id)
    return redirect(url_for('multas'))



if __name__ == '__main__':
    app.run( debug=True, port=80, host='0.0.0.0')