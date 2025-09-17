from builders.Seleccionador import Seleccionador

def main():
    
        selec = Seleccionador( )

        n = int(input("tamaño de cuadro: "))
        cuadro = selec.seleccionar(n)
        
        print(f"\nCuadrado mágico de orden {n}:")
        print(cuadro)  # gracias a __str__, imprime formateado

        print("\nComprobación:")

        if cuadro.validate():
            print("\nEs un cuadrado mágico válido.")
        else:
            print("\nNo cumple con las condiciones.")
if __name__ == "__main__":
    main()

