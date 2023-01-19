from data.modelo.vehiculo import Vehiculo
from flask import request

class AddDao():
    def __init__(self, db):
        self.db = db

    def addvehiculo(self, vehiculo):

        cursor = self.db.cursor()
        cursor.execute('INSERT INTO vehiculos ( marca, modelo, ano, color, matricula) VALUES ( %s, %s, %s, %s, %s)', ( marca, modelo, ano, color, matricula))
        self.db.commit()