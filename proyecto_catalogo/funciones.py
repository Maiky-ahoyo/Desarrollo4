import csv
import os

def procesa_csv(nombre_archivo:str)->list:
    '''
    Carga archivo csv y regresa una lista con diccionarios de revistas
    '''
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        lista = list(csv.DictReader(archivo, delimiter=';'))
    return lista

def crea_dict_areas(revistas:list)->dict:
    ''' Crea diccionario de areas a partir de 
        la lista de revistas
    '''
    d = {}
    for revista in revistas:
        key = revista["Areas/Categories"]
        key = key.split(":")[0].strip("' { '")
        if key in d:
            d[key].append(revista)
        else:
            d[key] = [revista]
    d_sorted = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}        
    return d_sorted

def crea_dict_categorias(revistas:list)->dict:
    ''' Crea diccionario de categorias a partir de 
        la lista de revistas
    '''
    d = {}
    for revista in revistas:
        key = revista["Areas/Categories"]
        key = key.split(":")[1].split(",")
        for categoria in key:
            categoria = categoria.strip("[ ' ' ] }")
            if categoria in d:
                d[categoria].append(revista)
            else:
                d[categoria] = [revista]
    d_sorted = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    return d_sorted

def crea_dict_catalogos(revistas:list)->dict:
    ''' Crea diccionario de catalogos a partir de 
        la lista de revistas
    '''
    d = {}
    revistas_sorted = sorted(revistas, key=lambda x: x["Catalogue"],reverse=False)
    for revista in revistas_sorted:
        key = revista["Catalogue"]
        if key in d:
            d[key].append(revista)
        else:
            d[key] = [revista]
    return d

def crea_dict_editoriales(revistas:list)->dict:
    ''' Crea diccionario de editoriales a partir de 
        la lista de revistas
    '''
    d = {}
    revistas_sorted = sorted(revistas, key=lambda x: x["Publisher"],reverse=False)
    for revista in revistas_sorted:
        key = revista["Publisher"]
        if key in d:
            d[key].append(revista)
        else:
            d[key] = [revista]
    return d

def crea_diccionario_iniciales(revistas:list)->dict:
    ''' Crea diccionario de iniciales a partir de 
        la lista de revistas
    '''
    revistas_sorted = sorted(revistas, key=lambda x: x["Title"],reverse=False)
    d = {}
    for revista in revistas_sorted:
        key = revista["Title"]
        key = key[0]
        key = key.upper()
        if key in d:
            d[key].append(revista)
        else:
            d[key] = [revista]
    d_sorted = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    return d_sorted

def crea_diccionario_qs(revistas:list)->dict:
    ''' Crea diccionario de Q a partir de 
        la lista de revistas
    '''
    d = {}
    revistas_sorted = sorted(revistas, key=lambda x: x["Q"],reverse=False)
    for revista in revistas_sorted:
        key = revista["Q"]
        if key in d:
            d[key].append(revista)
        else:
            d[key] = [revista]
    return d

def crea_dict_palabras_clave(revistas:list, inicial:str)->dict:
    ''' Crea diccionario de palabras clave a partir de 
        la lista de revistas
    '''
    d = {}
    for revista in revistas:
        key = revista["Title"]
        key = key.split(" ")
        for palabra in key:
            palabra = palabra.upper()
            if palabra.startswith(inicial):
                if palabra in d:
                    d[palabra].append(revista)
                else:
                    d[palabra] = [revista]
    return d

def busqueda_palabra(palabras:str, revistas:list)->list:
    ''' Crea una lista de revistas 
        a partir de la lista de revistas 
        y una/s palabras clave
    '''
    l = []
    revistas_sorted = sorted(revistas, key=lambda x: x["Title"],reverse=False)
    for revista in revistas_sorted:
        palabras = palabras.upper()
        titulo = revista["Title"].upper()
        if palabras in titulo:
            l.append(revista)
    return l        

def busqueda_rango_sjr(sjr1:float, sjr2:float, revistas:list)->list:
    ''' Crea una lista de revistas 
        a partir de la lista de revistas 
        y un rango de sjr
    '''
    l = []
    revistas_sorted = sorted(revistas, key=lambda x: x["SJR"],reverse=False)
    if sjr1 > sjr2:
        sjr_mayor = sjr1
        sjr_menor = sjr2
    else:
        sjr_mayor = sjr2 + 0.001
        sjr_menor = sjr1
    for revista in revistas_sorted:
        sjr = float(revista["SJR"])
        if sjr >= sjr_menor and sjr <= sjr_mayor:
            l.append(revista)
    return l

def paginacion(lista:list, pagina:int)->list:
    ''' Crea una lista de revistas 
        a partir de la lista de revistas 
        y un numero de pagina
    '''
    inicio = (int(pagina) - 1) * 50
    fin = inicio + 50
    return lista[inicio:fin]

if __name__ == "__main__":
    os.system('cls')
    revistas = procesa_csv('revistas.csv')
    areas = crea_dict_areas(revistas)
    categorias = crea_dict_categorias(revistas)
    catalogos = crea_dict_catalogos(revistas)
    editoriales = crea_dict_editoriales(revistas)
    iniciales = crea_diccionario_iniciales(revistas)
    qs = crea_diccionario_qs(revistas)
    total_paginas = len(revistas) // 50
    print(total_paginas)