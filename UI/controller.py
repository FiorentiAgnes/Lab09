import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza_aeroporti(self, e):
        #input
        dist_min_str = self._view.txt_distanza_minima.value
        try:
            dist_min = float(dist_min_str)
        except ValueError:
            self._view.create_alert("Inserire un valore numerico per la distanza.")
            return

        #Creazione Grafo
        self._model.buildGraph(dist_min)

        #Output risultati
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Grafo creato con {self._model.get_num_nodi()} vertici e {self._model.get_num_archi()} archi.")
        )

        #Stampiamo l'elenco degli archi
        archi = self._model.get_elenco_archi()
        for a in archi:
            self._view.txt_result.controls.append(ft.Text(a))

        self._view.update_page()