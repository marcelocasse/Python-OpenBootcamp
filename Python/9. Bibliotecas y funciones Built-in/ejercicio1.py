"""
Crea un script que le pida al usuario una lista de países (separados por comas). 
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

"""

def main():
    args = list(input("Ingrese países separando cada país por ,: ").lower().split(","))
    
    args = [x.strip() for x in args]

    args = sorted(list(set(args)))

    print(",".join(args))

if __name__ == "__main__":
    main()