from data.modelo.multas import Multa

class MultaDao():
    def __init__(self,db) -> None:
        self.db = db

    def dameTodasLasMultas(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM multas')
        data = cursor.fetchall()
        multas = []

        for multa in data:
            multas.append(Multa(multa[1], multa[2], multa[3], multa[4], multa[0]))

        return multas

    def addmulta(self, multa):
            
            cursor = self.db.cursor()
            cursor.execute('INSERT INTO multas ( fecha, lugar, descripcion, id_vehiculo) VALUES ( %s, %s, %s, %s)', ( multa.fecha, multa.lugar, multa.descripcion, multa.id_vehiculo))
            self.db.commit()


    def deletemulta(self,id):
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM multas WHERE id = %s',[id])
        self.db.commit()