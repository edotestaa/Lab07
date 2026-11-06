from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        result2 = []

        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")
            cursor = cnx.cursor()
            query = "SELECT DISTINCT genere FROM libro ORDER BY genere ASC"
            cursor.execute(query)
            for row in cursor:
                result2.append(row[0])

            cursor.close()
            cnx.close()
        return result2

