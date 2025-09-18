# builders/double_even_builder.py  (versión que sigue tu imagen)

from magic_square import MagicSquare

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

        



        
