"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos
impares de una lista pasada por parámetro con filter y realizará una suma de todos 
estos elementos obtenidos mediante reduce.
"""
from functools import reduce

def filtrado_impar(numlista:list):
    return list(filter(lambda x : (x %2 ==1) ,numlista))
def main():
    
    numeros_impares = filtrado_impar(list(range(1,101)))
    
    sumatotal = reduce(lambda a,b: a+b,numeros_impares)

    print(sumatotal)
    

if __name__ == "__main__":
    main()