# builders/double_even_builder.py  (versión que sigue tu imagen)

from magic_square import MagicSquare
from builders.odd_builder import OddMagicSquareBuilder

class EvenMagicSquareBuilder:
    """Construye un cuadrado mágico para n múltiplo de 4."""

    def doublebuild(self, n: int) -> MagicSquare:
        

        square = MagicSquare(n)
        b = n // 4

        # marcar bloques diagonales
        marked = [[False] * n for _ in range(n)]
        for bi in range(4):
            for bj in range(4):
                if bi == bj or (bi + bj == 3):
                    for i in range(bi * b, bi * b + b):
                        for j in range(bj * b, bj * b + b):
                            marked[i][j] = True

        # 1) colocar números en celdas marcadas (en orden natural)
        used = []   # ahora usamos lista
        for k in range(1, n * n + 1):
            i = (k - 1) // n
            j = (k - 1) % n
            if marked[i][j]:
                square.matrix[i][j] = k
                used.append(k)

        # 2) rellenar celdas vacías con los números restantes en orden descendente SIN sort
        unused = []
        for k in range(1, n * n + 1):
             if k not in used:    # comprobamos uno por uno
                 unused.append(k)

        idx = len(unused) - 1
        for i in range(n):
         for j in range(n):
            if square.matrix[i][j] == 0:
                square.matrix[i][j] = unused[idx]
                idx -= 1

        return square

    def singlebuild(self, n : int)-> MagicSquare:
        #Dividir en cuadrantes
        square = MagicSquare(n)
        
        k = n//2

        mini_builder = OddMagicSquareBuilder()
        cuadrado_base = mini_builder.build(k)
                 
        # --- Llenado de Cuadrantes ---
        offset_B = k * k 
        offset_C = 2 * k * k
        offset_D = 3 * k * k
        
        
        for i in range(n):
            for j in range(n):
                i_base = i % k
                j_base = j % k
                valor_base = cuadrado_base.matrix[i_base][j_base]
    
                if i < k and j < k:
                    square.matrix[i][j] = valor_base
                elif i >= k and j < k:                     
                    square.matrix[i][j] = valor_base + offset_D
                elif i < k and j >= k:
                    square.matrix[i][j] = valor_base + offset_C
                elif i >= k and j >= k:
                    square.matrix[i][j] = valor_base + offset_B
                
        if n == 6:
            # Intercambio para la casilla (0, 0) de A y D
            temp = square.matrix[0][0]
            square.matrix[0][0] = square.matrix[3][0]
            square.matrix[3][0] = temp

            # Intercambio para la casilla (1, 1) de A y D
            temp = square.matrix[1][1]
            square.matrix[1][1] = square.matrix[4][1]
            square.matrix[4][1] = temp
            
            # Intercambio para la casilla (2, 0) de A y D
            temp = square.matrix[2][0]
            square.matrix[2][0] = square.matrix[5][0]
            square.matrix[5][0] = temp
        elif n > 6:
  
            # --- Intercambio Izquierdo (A <-> D) ---
            # Para n=10, k=5. Columnas a cambiar: k//2 = 2
            m = k // 2
            for i in range(k):
                for j in range(m):
                    # Intercambiamos las primeras 'm' columnas completas
                    temp = square.matrix[i][j]
                    square.matrix[i][j] = square.matrix[i + k][j]
                    square.matrix[i + k][j] = temp
            
            # --- Intercambio Derecho (C <-> B) ---
            fila_central = k // 2
            for i in range(k):
                if i != fila_central:
                    j_real = n - 1
                    temp = square.matrix[i][j_real]
                    square.matrix[i][j_real] = square.matrix[i + k][j_real]
                    square.matrix[i + k][j_real] = temp

            j_real = n - 2
            temp = square.matrix[fila_central][j_real]
            square.matrix[fila_central][j_real] = square.matrix[fila_central + k][j_real]
            square.matrix[fila_central + k][j_real] = temp
                    
        return square


        
