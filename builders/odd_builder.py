    # builders/odd_builder.py: Lógica para construir cuadrados impares.
# builders/odd_builder.py
from builders.builder import MagicSquareBuilder
from magic_square import MagicSquare

class OddMagicSquareBuilder(MagicSquareBuilder):

    def build(self, n: int) -> MagicSquare:
       
        square = MagicSquare(n)

        i = 0
        j = n // 2
        
        # Iteramos desde el número 1 hasta n*n
        for num in range(1, n * n + 1):
            
            square.matrix[i][j] = num

            
            i_siguiente = (i - 1 + n) % n
            j_siguiente = (j + 1) % n

            
            if square.matrix[i_siguiente][j_siguiente] != 0:
                
                i = (i + 1 + n) % n
            else:
              
                i = i_siguiente
                j = j_siguiente

        
        return square
    
    
