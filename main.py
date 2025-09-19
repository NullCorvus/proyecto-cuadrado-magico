from builders.Seleccionador import Seleccionador

def main():
    
    while True:
        selec = Seleccionador( )
        try:
            n = int(input("tamaño de cuadro: ")) 

        except ValueError:
            print("El tamaño ingresado debe ser un número entero positivo")

            return False
        if n < 1:
            print("El tamaño ingresado debe ser un número entero positivo")

            return False
        
        cuadro = selec.seleccionar(n)
        
        print(f"\nCuadrado mágico de orden {n}:")
        print(cuadro)  # ya imprime formateado gracias al muy humilde __str__

        print("\nComprobación:")

        if cuadro.validate():
            print("\nEs un cuadrado mágico válido.")
        else:
            print("\nNo cumple con las condiciones.")
if __name__ == "__main__":
    main()

