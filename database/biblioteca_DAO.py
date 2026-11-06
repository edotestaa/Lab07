from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        result = []

        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")
            cursor = cnx.cursor()
            query = "SELECT * FROM biblioteca ORDER BY nome ASC"
            cursor.execute(query)
            for row in cursor:
                result.append(Biblioteca(*row))

            cursor.close()
            cnx.close()
        return result
