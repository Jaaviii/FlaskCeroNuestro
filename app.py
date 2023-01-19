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
    
    vehiculo_dao : VehiculoDao = VehiculoDao(db)
   
    return render_template('index.html' , vehiculos = vehiculo_dao.dameTodosLosVehiculos())


@app.route('/addvehiculo', methods=['POST'])
def addvehiculo():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = request.form['ano']
        color = request.form['color']
        matricula = request.form['matricula']

        vehiculo = Vehiculo(marca, modelo, ano, color, matricula)
    
        return redirect(url_for('Index'))
    

@app.route('/deletevehiculo/<string:id>')
def delete(id):
    #cursor = db.cursor()
    #cursor.execute('DELETE FROM vehiculos WHERE id = {0}'.format(id))
    #db.commit()
    return redirect(url_for('Index'))



if __name__ == '__main__':
    app.run( debug=True)