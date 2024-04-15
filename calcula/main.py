'''
Calcula datos estadísticos de una lista de números, usando argumentos
'''

import argparse
import os
import calcula

def main(listado:list, operacion:str):
    diccionario = {"suma":"print(f'{calcula.suma(listado)}')", 
                   "promedio":"print(f'{calcula.promedio(listado)}')", 
                   "moda":"print('{calcula.moda(listado)}')",
                   "todos":"print('Sin implementar')"}
    eval(diccionario[operacion])
    if operacion in diccionario:
        print(f"La {operacion} de {listado} es {eval(diccionario[operacion])}")
    else:
        print("Operación no implementada")
    '''
    operacion = operacion.lower()
    if operacion == "suma":
        print(f"La suma de {listado} es {calcula.suma(listado)}")
    if operacion == "promedio":
        print(f"El promedio de {listado} es {calcula.promedio(listado)}")
    if operacion == "moda":
        print(f"La moda de {listado} es {calcula.moda(listado)}")
    if operacion == "todos":
        print(f"La suma de {listado} es {calcula.suma(listado)}")
        print(f"El promedio de {listado} es {calcula.promedio(listado)}")
        print(f"La moda de {listado} es {calcula.moda(listado)}")  
    '''  

if __name__ == "__main__":
    os.system("cls")
    #declaramos nuestro parser o procesador de argumentos
    parser = argparse.ArgumentParser(description="Calcula datos estadísticos de una lista de números")
    parser.add_argument("enteros", metavar = "N", type = int, nargs = "+", help = "")
    parser.add_argument("--operacion", "-o", dest = "o", type = str, 
                        choices = ["suma", "promedio", "moda", "todos"])
    args = parser.parse_args()
    print(args.enteros)
    print(args.o)
    main(args.enteros, args.o)
