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
            vehiculos.append(Vehiculo(vehiculo[1], vehiculo[2], vehiculo[3], vehiculo[4], vehiculo[5], vehiculo[0]))

        return vehiculos
    
    def addvehiculo(self, vehiculo):

        cursor = self.db.cursor()
        cursor.execute('INSERT INTO vehiculos ( marca, modelo, ano, color, matricula) VALUES ( %s, %s, %s, %s, %s)', ( vehiculo.marca, vehiculo.modelo, vehiculo.ano, vehiculo.color, vehiculo.matricula))
        self.db.commit()

 
    def deletevehiculo(self,id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM vehiculos WHERE id = %s",[id])
        self.db.commit()

