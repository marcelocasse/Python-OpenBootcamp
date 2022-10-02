def anio_bisiesto(anio):
    if anio%4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

anio_bisiesto(int(input("Ingrese un año para saber si es bisiesto: ")))