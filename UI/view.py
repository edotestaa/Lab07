import flet as ft
from flet import MainAxisAlignment
from flet.controls import alignment

from model.model import Model
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self._controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self._controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        risultati = self._controller.get_biblioteche()
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self.dd_biblioteche = ft.Dropdown(label = "Biblioteche", width= 300)
        self.dd_biblioteche.options.append(risultati)
        self.dd_generi = ft.Dropdown(label = "Generi", width= 200)

        # Sezione 3: Libri
        self._list_view = ft.ListView(expand=True, spacing=10)


        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row([self.dd_biblioteche,self.dd_generi], alignment = MainAxisAlignment.CENTER, spacing= 80),

            # Sezione 3: Libri
            ft.Row([ft.Button("Mostra Libri")], alignment = MainAxisAlignment.CENTER),
            self._list_view,
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
