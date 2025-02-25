# Proyecto Laberinto

Este proyecto implementa la resolución de un laberinto utilizando distintos algoritmos de búsqueda.

## Estructura del Proyecto

- **`laberinto.txt`**: Archivo que contiene la representación del laberinto.
- **`main.py`**: Código principal que ejecuta los algoritmos de búsqueda.
- **`grafo.py`**: Implementación de la estructura de datos para el grafo.

## Formato del Archivo `laberinto.txt`

El archivo de entrada sigue esta estructura:

1. La primera línea contiene las dimensiones del laberinto en formato `(N, M)`.
2. Las siguientes líneas contienen la matriz representando el laberinto con los siguientes valores:
   - `0`: Camino libre
   - `1`: Pared
   - `2`: Punto de inicio
   - `3`: Meta

Ejemplo:
```
(10,10)
[2, 1, 0, 0, 1, 1, 0, 1, 0, 3]
[0, 0, 1, 0, 0, 1, 1, 0, 1, 0]
...
```

## Algoritmos Implementados

- **Búsqueda en Anchura (BFS)**
- **Búsqueda en Profundidad (DFS)**
- **Algoritmo A***

## Uso

Ejecutar el siguiente comando para correr el programa:

```bash
python main.py
```

Asegúrate de que el archivo `laberinto.txt` esté en la misma carpeta que `main.py`.

## Requisitos

- Python 3.x
- Librerías estándar (no requiere instalaciones adicionales)


