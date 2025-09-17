    # builders/odd_builder.py: Lógica para construir cuadrados impares.
# builders/odd_builder.py
from builders.builder import MagicSquareBuilder
from magic_square import MagicSquare

class OddMagicSquareBuilder(MagicSquareBuilder):
    """Construye un cuadrado mágico para órdenes impares (n = 3, 5, 7...)."""

    def build(self, n: int) -> MagicSquare:
        # --- PASO 1: Crear un objeto MagicSquare vacío ---
        # En este punto, square.matrix es una cuadrícula de n x n llena de ceros.
        square = MagicSquare(n)

        # --- PASO 2: Rellenar la matriz DENTRO del objeto 'square' ---
        # Implementación del algoritmo de La Loubère.

        # Empezamos en la casilla central de la fila superior.
        i = 0
        j = n // 2
        
        # Iteramos desde el número 1 hasta n*n
        for num in range(1, n * n + 1):
            # Colocamos el número actual directamente en la matriz del objeto.
            square.matrix[i][j] = num

            # Calculamos la posición del siguiente número:
            # Arriba y a la derecha.
            i_siguiente = (i - 1 + n) % n
            j_siguiente = (j + 1) % n

            # Si la casilla siguiente ya está ocupada...
            if square.matrix[i_siguiente][j_siguiente] != 0:
                # ...nos movemos una casilla hacia abajo.
                i = (i + 1 + n) % n
            else:
                # ...si no, nos movemos a la casilla calculada.
                i = i_siguiente
                j = j_siguiente

        # --- PASO 3: Devolver el objeto 'square' ya rellenado ---
        return square
    
    
