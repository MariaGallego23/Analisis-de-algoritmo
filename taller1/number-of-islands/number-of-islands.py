# Ejercicio 2: 200. Number of Islands  
# Familia: grafos
# https://leetcode.com/problems/number-of-islands/
#
# MODELO: grafo no dirigido implícito en la grilla.
#   - Vértice: cada celda '1'.
#   - Arista: entre celdas '1' vecinas en las 4 direcciones (sin diagonales).
#   - Contar islas = contar componentes conexas.

from collections import deque

class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])   # m filas, n columnas
        count = 0                        # número de componentes 

        #4 direcciones: abajo, arriba, derecha, izquierda.
        direcciones = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(m):
            for j in range(n):
                # Las celdas '0' (agua) no se recorren como vértices.
                if grid[i][j] == '1':
                    # Encontramos una isla nueva (no visitada).
                    count += 1
                    grid[i][j] = '0'          # marcar como visitada ("hundirla")
                    cola = deque([(i, j)])

                    #visita toda la componente de esta celda.
                    while cola:
                        x, y = cola.popleft()
                        for dx, dy in direcciones:
                            a, b = x + dx, y + dy
                            # Dentro de la grilla y tierra sin visitar
                            if 0 <= a < m and 0 <= b < n and grid[a][b] == '1':
                                grid[a][b] = '0'   # marcar evita duplicados
                                cola.append((a, b))
        return count

# Complejidad: tiempo Θ(m·n) (cada celda se visita una vez),
#              espacio O(m·n) en el peor caso (la cola).
