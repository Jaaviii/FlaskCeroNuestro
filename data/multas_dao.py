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
            multas.append(Multa(multa[0], multa[1], multa[2], multa[3], multa[4]))

        return multas