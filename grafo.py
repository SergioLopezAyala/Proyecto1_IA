import heapq
import ast

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

def leer_laberinto_desde_archivo(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    dimensiones = ast.literal_eval(lineas[0].strip())
    laberinto = [ast.literal_eval(linea.strip()) for linea in lineas[1:]]
    return dimensiones, laberinto

def encontrar_posiciones(laberinto, valor):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == valor:
                return (i, j)

def generar_grafo(laberinto):
    filas, columnas = len(laberinto), len(laberinto[0])
    grafo = {}
    movimientos = [(0,1), (1,0), (0,-1), (-1,0)]
    
    for i in range(filas):
        for j in range(columnas):
            if laberinto[i][j] != 1:  # No es una pared
                grafo[(i, j)] = []
                for dx, dy in movimientos:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] != 1:
                        grafo[(i, j)].append((nx, ny))
    return grafo

def main():
    archivo_laberinto = "laberinto.txt"
    dimensiones, laberinto = leer_laberinto_desde_archivo(archivo_laberinto)
    inicio = encontrar_posiciones(laberinto, 2)
    meta = encontrar_posiciones(laberinto, 3)
    grafo_dict = generar_grafo(laberinto)
    grafo = Grafo(grafo_dict)
    
    print("BFS:", grafo.primero_anchura(inicio, meta))
    print("DFS:", grafo.primero_profundidad(inicio, meta))
    print("A*:", grafo.a_estrella(inicio, meta))

if __name__ == "__main__":
    main()
