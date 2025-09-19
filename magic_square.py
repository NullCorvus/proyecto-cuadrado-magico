
class MagicSquare:
  

    def __init__(self, n: int):
        
        self.n = n

        
        self.matrix = [[0] * n for _ in range(n)]

        # Calcula y almacena la constante mágica 
        # La fórmula es: n * (n^2 + 1) / 2
        self.magic_constant = n * (n**2 + 1) // 2

    def validate(self) -> bool:
    
        print(f"\nConstante mágica esperada: {self.magic_constant}\n")

        # Validar filas
        for i, fila in enumerate(self.matrix):
            suma_fila = sum(fila)
            print(f"Suma fila {i+1}: {suma_fila}")
            if suma_fila != self.magic_constant:
                return False

        # Validar columnas
        for j in range(self.n):
            suma_col = sum(self.matrix[i][j] for i in range(self.n))
            print(f"Suma columna {j+1}: {suma_col}")
            if suma_col != self.magic_constant:
                return False

        # Diagonal principal
        suma_diag1 = sum(self.matrix[i][i] for i in range(self.n))
        print(f"Suma diagonal principal: {suma_diag1}")
        if suma_diag1 != self.magic_constant:
            return False

        # Diagonal secundaria
        suma_diag2 = sum(self.matrix[i][self.n - 1 - i] for i in range(self.n))
        print(f"Suma diagonal secundaria: {suma_diag2}")
        if suma_diag2 != self.magic_constant:
            return False

        return True



    def __str__(self) -> str:
       
        output = ""
        for row in self.matrix:
            for number in row:
                
                output += f"{number:4}"  # :4 significa "ocupa 4 espacios"
            output += "\n"  # Añade un salto de línea al final de cada fila.
        return output
