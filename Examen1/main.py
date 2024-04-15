from gettext import Catalog
import os
from Revista import Revista

class main:
     
    def lee_archivo(archivo:str)->list:
        with open(archivo,"r",encoding  = "utf8") as archivo:
            lista = archivo.readlines()
        return lista
    
    def crear_catalogo(lista:list, catalogo:str)->list:
        lista_cat = []
        for linea in lista:
            linea = linea.strip()
            revista = Revista(linea,catalogo)
            lista_cat.append(revista)
        return lista_cat
    
    def crear_dict(lista:list)->dict:
        diccionario = {}
        for revista in lista:
            titulo = revista
            palabras = titulo.split()
            for palabra in palabras:
                if palabra in diccionario:
                    diccionario[palabra].add(revista)
                else:
                    diccionario[palabra] = set()
                    diccionario[palabra].add(revista)
            if titulo in diccionario:
                diccionario[titulo].add(revista)
            else:
                diccionario[titulo] = set()
                diccionario[titulo].add(revista)
        return diccionario
    
    if __name__ == '__main__':
        os.system("cls")
        lista = lee_archivo("CONACYT_RadGridExport.csv")
        catalogo = crear_catalogo(lista,"CONACYT")
        diccionario = crear_dict(catalogo)
        for k,v in diccionario.items():
            print(f'{k} - {v}')
