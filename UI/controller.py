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

    def get_biblioteche(self):
        return self._model.get_biblioteche()
    def get_generi(self):
        return self._model.get_generi()

    def seleziona_genere(self, e):
        valore = e.control.value
        if (valore == "Nessun filtro" or not valore):
         self.genere_selezionato = None
        else:
            self.genere_selezionato = valore
    def seleziona_biblioteca(self, e):
        valore = e.control.value
        if (valore == "Nessun filtro" or not valore):
             self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = valore

    def mostra_libri(self, e):
        valore_bib = self._view.dd_biblioteche.value
        valore_gen = self._view.dd_generi.value
        if valore_bib == "Nessun filtro" or not valore_bib:
            filtro_bib = None
        else:
            filtro_bib = valore_bib
        if valore_gen == "Nessun filtro" or not valore_gen:
            filtro_gen = None
        else:
            filtro_gen = valore_gen
        libri = self._model.get_libri_filtrati(filtro_bib, filtro_gen)

        self._view._list_view.controls.clear()
        if not libri:
            self._view.show_alert("Nessun libro soddisfa i filtri selezionati")
            self._view.update()
            return
        titoli_mostrati = set()
        for libro in libri:
            identificativo = (libro.titolo, libro.autore)

            if filtro_bib is None and identificativo in titoli_mostrati:
                continue

            titoli_mostrati.add(identificativo)
            self._view._list_view.controls.append(
                ft.Text(f"📖 {libro.titolo} — {libro.autore} ({libro.genere})", size=14)
            )
        self._view.update()
