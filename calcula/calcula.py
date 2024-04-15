'''
Calcula diferentes tipos de funciones estadísticas
en un alista de numeros
'''

import os


def suma(lista:list)->int:
    '''
    Suma los elementos de una lista
    '''
    return sum(lista)

def promedio(lista:list)->float:
    '''
    Calcula el promedio de una lista
    '''
    return suma(lista)/len(lista)

def moda(lista:list)->int:
    '''
    Calcula la moda de una lista
    '''
    dic = {x:0 for x in lista}
    for x in lista:
        dic[x] += 1
    m = max(dic, key = lambda key:dic[key])
    return m    

def main(lista:list):
    print(f"La suma de {lista} es {suma(lista)}")
    print(f"El promedio de {lista} es {promedio(lista)}")
    print(f"La moda de {lista} es {moda(lista)}")

if __name__ == "__main__":
    os.system("cls")
    lista = [1,3,5,48,26,23,19,15,156,161,56,456,61,16,565,4,68,3]
    main(lista)