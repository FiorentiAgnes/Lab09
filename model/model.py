
import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}  #ID -> Oggetto Aeroporto

    def buildGraph(self, x):
        self._grafo.clear()

        #tutti gli aeroporti e riempio la mappa
        tutti_aeroporti = DAO.get_all_nodes()
        for a in tutti_aeroporti:
            self._idMap[a.ID] = a

        #Aggiungo i nodi al grafo (gli oggetti Airport stessi)
        self._grafo.add_nodes_from(tutti_aeroporti)

        #Recupero gli archi (solo ID e peso)
        rotte = DAO.getAllEdgesPesati(x)

        for u_id, v_id, peso in rotte:
            #Recupero gli oggetti Aeroporto dalla mappa usando gli ID
            u = self._idMap[u_id]
            v = self._idMap[v_id]

            #Aggiungo l'arco tra gli oggetti
            self._grafo.add_edge(u, v, weight=peso)

    def get_num_nodi(self):
        return self._grafo.number_of_nodes()

    def get_num_archi(self):
        return self._grafo.number_of_edges()

    def get_elenco_archi(self):
        #Restituisce gli archi con il loro peso
        result = []
        for u, v, data in self._grafo.edges(data=True):
            result.append(f"{u} <-> {v} | Distanza media: {data['weight']:.2f}")
        return result