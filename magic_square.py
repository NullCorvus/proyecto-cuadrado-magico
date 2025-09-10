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
        Debe sumar las filas, columnas y las dos diagonales principales.
        Retorna True si es mágico, False si no lo es.
        """
        # --- Lógica de validación que debes implementar ---
        # 1. Sumar cada fila y comprobar si es igual a self.magic_constant.
        # 2. Sumar cada columna y comprobar.
        # 3. Sumar la diagonal principal y comprobar.
        # 4. Sumar la diagonal secundaria y comprobar.

        print(f"Validando... La suma debería ser {self.magic_constant}")
        # Por ahora, devolvemos True. Deberás completar la lógica.
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
