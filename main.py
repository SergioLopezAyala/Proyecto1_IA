import ast
from grafo import Grafo

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
