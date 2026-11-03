from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self,e):
        db = DBConnect()
        cnx = db.get_connection()
        if cnx is not None:
            print("Connection established")
            query = "SELECT nome FROM biblioteca"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                biblioteche = Biblioteca(*row)
                result.append(biblioteche)

            cursor.close()
            cnx.close()
        return result
