import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
   # def handler_dd_biblioteca (self,e):
    def get_biblioteche(self):
        return self._model.get_biblioteche()
    def get_generi(self):
        return self._model.get_generi()

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO
