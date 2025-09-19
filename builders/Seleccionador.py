from builders.even_builder import EvenMagicSquareBuilder
from builders.odd_builder import OddMagicSquareBuilder
class Seleccionador:


    def seleccionar(self, n):
        
            if n % 2 == 1:
                # Método para impares
                odd = OddMagicSquareBuilder()
                return odd.build(n)
            
            elif n % 4 == 0:
                # Método para pares dobles (n divisible entre 4)
                even = EvenMagicSquareBuilder()
                return even.doublebuild(n)
            
            elif n % 2 == 0 and n % 4 != 0:
                # Método para pares simples (los verdes)
                even  = EvenMagicSquareBuilder()
                return even.singlebuild(n)
            
            else:
                raise ValueError("El tamaño ingresado no es válido para construir un cuadrado mágico")

    
