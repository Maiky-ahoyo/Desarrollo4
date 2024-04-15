import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
from revist import Revista
import json

#222214253 Arroyo Lopez Miguel Angel 05/04/2024

def leer_url(archivo):
    urls = []
    with open(archivo, 'r') as txt:
        for linea in txt:
            urls.append(linea)
    return urls

def procesar_html(url):
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    return soup

def extraer_datos(soup):
    body = soup.find('tbody')
    datos = []
    revistas = []
    for row in body.find_all('tr') :
        datosbody = []
        for col in row.find_all('td'):
            datosbody.append(col.text.strip())
        datos.append(datosbody)
    for dato in datos:
        titulo = dato[1]
        catalogo = dato[2]
        sjr_q = dato[3].split(' ')
        sjr = sjr_q[0]
        q = sjr_q[1]
        h_index = dato[4]
        total_citas = dato[8]
        revistas.append([titulo,catalogo,sjr,q,h_index,total_citas])
    return revistas
              
def h_index_menor_a(revistas, h_index):
    revistas_filtradas = []
    for revista in revistas:
        if int(revista[4]) < h_index:
            revistas_filtradas.append(revista)
    return revistas_filtradas

def crear_revista(revista):
    revista_nueva = Revista(titulo = revista[0],catalogo = revista[1],sjr = revista[2], 
                      q = revista[3],h_index =revista[4],total_citas = revista[5])
    return revista_nueva

def crear_json(revistas):
    with open('revistas.json', 'w') as file:
        for revista in revistas:
            file.write(repr(revista)+'\n')
    print(f'Archivo {file} guardado')
        

if __name__ == "__main__":
    os.system('cls')
    urls = leer_url('urls.txt')
    revistas = []
    for url in urls:
        html = procesar_html(url)
        informacion = extraer_datos(html)
        for dato in informacion:
            nueva = crear_revista(dato)
            revistas.append(nueva)
            print(f'Revista: {dato}')
    revistas_filtradas = h_index_menor_a(informacion, 100)       
    for revista in revistas_filtradas:
        print(f'Revista filtrada: {revista}')
    crear_json(revistas)    