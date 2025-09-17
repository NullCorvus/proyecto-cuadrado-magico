# magic_square.py: Define la clase MagicSquare (almacena la matriz y valida).
# magic_square.py

class MagicSquare:
    """
    Representa un cuadrado mágico ya construido.
    Su función es contener la matriz de números y ofrecer
    métodos para validarla e imprimirla.
    """

    def __init__(self, n: int):
        # Almacena el tamaño del cuadrado (ej. 3 para un 3x3)
        self.n = n

        # Crea una matriz (lista de listas) de n x n, toda llena de ceros al principio.
        # Esta matriz será llenada por uno de los 'builders'.
        self.matrix = [[0] * n for _ in range(n)]

        # Calcula y almacena la constante mágica que se espera para este tamaño.
        # La fórmula es: n * (n^2 + 1) / 2
        self.magic_constant = n * (n**2 + 1) // 2

    def validate(self) -> bool:
        """
        Verifica si la matriz cumple con las condiciones de un cuadrado mágico.
        Imprime las sumas de filas, columnas y diagonales.
        """
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
        """
        Prepara una versión en texto del cuadrado para poder imprimirlo con print().
        """
        # Se construye un string con el contenido de la matriz, bien formateado.
        output = ""
        for row in self.matrix:
            for number in row:
                # Añade cada número al string, con un espaciado para que se alinee.
                output += f"{number:4}"  # :4 significa "ocupa 4 espacios"
            output += "\n"  # Añade un salto de línea al final de cada fila.
        return output
