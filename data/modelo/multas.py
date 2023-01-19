#Creamos una clase en modelo con los campos de la base de datos. 
#Esto lo que hace es convertir los datos de la base de datos en variables de python

class Multa():
    
        def __init__(self, id : int, id_vehiculo : int, fecha : str, importe : float, descripcion : str):
    
            self.id = id
            self.id_vehiculo = id_vehiculo
            self.fecha = fecha
            self.importe = importe
            self.descripcion = descripcion
