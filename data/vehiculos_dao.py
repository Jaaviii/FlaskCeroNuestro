from data.modelo.vehiculo import Vehiculo

class VehiculoDao():


    def __init__(self,db) -> None:
        self.db = db

    def dameTodosLosVehiculos(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM vehiculos')
        data = cursor.fetchall()
        vehiculos = []

        for vehiculo in data:
            vehiculos.append(Vehiculo(vehiculo[0], vehiculo[1], vehiculo[2], vehiculo[3], vehiculo[4], vehiculo[5]))

        return vehiculos

    def delete(self,db):
        cursor = db.cursor()
        cursor.execute('DELETE FROM vehiculos WHERE id = {0}'.format(id))
        db.commit()
