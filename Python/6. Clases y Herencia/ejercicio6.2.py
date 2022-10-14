"""
En este segundo ejercicio, tendréis que crear un programa 
que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje 
con el resultado de la nota y si ha aprobado o no.
"""

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"{self.nombre} su nota es {self.nota}")

    def resultado_nota(self):
        if self.nota<5:
            print("El alumno no ha aprobado")
        else:
            print("El alumno ha aprobado")


alumno1 = Alumno("Mario",8)

alumno1.imprimir()

alumno1.resultado_nota()