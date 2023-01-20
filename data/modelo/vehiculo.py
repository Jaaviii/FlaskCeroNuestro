#Creamos una clase en modelo con los campos de la base de datos. 
#Esto lo que hace es convertir los datos de la base de datos en variables de python

class Vehiculo():

    def __init__(self, marca : str, modelo : str, ano : int, color : str, matricula : str,id : int = 0):

        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color
        self.matricula = matricula


        
