"""
En este segundo ejercicio, tendréis que crear un archivo py 
y dentro crearéis una clase Vehículo,
haréis un objeto de ella,lo guardaréis en un archivo y luego lo cargamos.
"""

import pickle

class Vehículo:
    
    def __init__(self,color,puertas):
        self.color = color
        self.puertas = puertas
    
    def __str__(self):
        return f'Este vehículo es de color {self.color} y tiene {self.puertas} puertas'

if __name__ == "__main__":

    Renault12 = Vehículo('Rojo','4')
    print(Renault12)

    f = open('vehiculo.dat','wb')

    pickle.dump(Renault12,f)

    f.close()

    f = open('vehiculo.dat','rb')

    nuevo_renault12 = pickle.load(f)

    f.close()

    print(nuevo_renault12)

