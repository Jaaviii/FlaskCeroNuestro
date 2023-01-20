#Creamos una clase en modelo con los campos de la base de datos. 
#Esto lo que hace es convertir los datos de la base de datos en variables de python

class Multa():
    
        def __init__(self,  fecha : str, lugar : str, descripcion : str, id_vehiculo : int, id : int = 0):
    
            self.id = id
            self.fecha= fecha
            self.lugar = lugar
            self.descripcion = descripcion
            self.id_vehiculo = id_vehiculo

