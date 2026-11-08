from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_generi()


    def get_biblioteche(self):
        return self._biblioteca_dao.get_biblioteche()

    def get_libri_filtrati(self, nome_biblioteca, genere):
        return self._libro_dao.get_libri_filtrati(nome_biblioteca, genere)
