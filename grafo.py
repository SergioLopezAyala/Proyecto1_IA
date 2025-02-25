import heapq

class Grafo:
    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia

    def obtener_vecinos(self, v):
        return self.lista_adyacencia.get(v, [])

    def h(self, n, meta):
        return abs(n[0] - meta[0]) + abs(n[1] - meta[1])

    def primero_profundidad(self, nodo_inicio, nodo_final, visitados=None, camino=None):
        if visitados is None:
            visitados = set()
        if camino is None:
            camino = []
        visitados.add(nodo_inicio)
        camino.append(nodo_inicio)
        if nodo_inicio == nodo_final:
            return camino
        for vecino in self.obtener_vecinos(nodo_inicio):
            if vecino not in visitados:
                resultado = self.primero_profundidad(vecino, nodo_final, visitados, camino[:])
                if resultado:
                    return resultado
        return None

    def primero_anchura(self, nodo_inicio, nodo_final):
        cola = [(nodo_inicio, [nodo_inicio])]
        visitados = set()
        while cola:
            nodo, camino = cola.pop(0)
            if nodo == nodo_final:
                return camino
            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in self.obtener_vecinos(nodo):
                    cola.append((vecino, camino + [vecino]))
        return None

    def a_estrella(self, nodo_inicio, nodo_final):
        cola = [(0, nodo_inicio, [])]
        visitados = set()
        while cola:
            costo, nodo, camino = heapq.heappop(cola)
            if nodo == nodo_final:
                return camino + [nodo]
            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in self.obtener_vecinos(nodo):
                    heapq.heappush(cola, (costo + 1 + self.h(vecino, nodo_final), vecino, camino + [nodo]))
        return None
