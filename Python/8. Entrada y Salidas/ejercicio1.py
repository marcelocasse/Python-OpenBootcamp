"""
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
lo abráis y escribáis dentro del archivo.
Para ello, tendréis que acceder dos veces al archivo creado.

"""

if __name__ == "__main__":
    f = open('archivo.txt','w')
    f.write('Primera linea\n')
    f.close()

    f = open('archivo.txt','r+')
    dato = f.read()
    print(dato)
    f.write('Segunda linea\n')
    f.close()