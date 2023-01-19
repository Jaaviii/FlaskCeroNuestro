from data.modelo.vehiculo import Vehiculo
from flask import request

class AddDao():
    def __init__(self, db):
        self.db = db

   