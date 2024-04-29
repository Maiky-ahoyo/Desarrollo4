import requests
from bs4 import BeautifulSoup as bs
import os
import csv

def procesar_html(url):
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    return soup

def extraer_datos(html):
    body = html.find('tbody')
    siguiente = html.find('div', class_='pagination_buttons')
    siguiente = siguiente.find_all('a')
    siguiente = siguiente[1]['href']
    siguiente = (f"https://www.scimagojr.com/{siguiente}")
    datos = []
    revista = []
    for row in body.find_all('tr') :
        datosbody = []
        for col in row.find_all('td'):
            datosbody.append(col)
        datos.append(datosbody)
    for dato in datos:
        link = dato[1].a['href']
        link = (f"https://www.scimagojr.com/{link}")
        titulo = dato[1].text
        catalogo = dato[2].text
        sjr_q = dato[3].text.split(' ')
        sjr = sjr_q[0]
        if len(sjr_q) > 1:
            q = sjr_q[1]
        else:
            q = 'N/A'    
        h_index = dato[4].text
        total_citas = dato[8].text
        info_adicional = extraer_info_adicional(link)
        sitio_web = info_adicional[0]
        areas = info_adicional[1]
        editorial = info_adicional[2]
        issn = info_adicional[3]
        widget = info_adicional[4]
        revista = [titulo, catalogo, sjr, q, h_index, total_citas, sitio_web, areas, editorial, issn, widget]
        print(revista)
        if not verificar_revista(titulo):
            print('Guardando revista...')
            escribir_csv(revista)
        else:
            print('Revista ya guardada...')
        print('-----------------------------------------------------')    
    new_html = procesar_html(siguiente)
    extraer_datos(new_html)      

def extraer_info_adicional(url):
    html = procesar_html(url)
    body = html.find('body')
    grid = body.find('div', class_='journalgrid')
    divs = []
    for div in grid.find_all('div'):
        divs.append(div)
    if divs[7].a:
        sitio_web = divs[7].a['href']
    else:
        sitio_web = 'N/A'
    areas = {}
    for area in divs[1].find_all('li'):
        if area.find_all('ul'):
            categorias = []
            for categoria in area.find_all('li'):
                categorias.append(categoria.a.text)
            areas[area.a.text] = categorias
    editorial = divs[2].find('a').text.strip()
    issn = divs[5].find('p').text.strip()
    widget = body.find('input', id='embed_code')
    widget = widget['value']
    return [sitio_web, areas, editorial, issn, widget]

def verificar_revista(titulo):
    with open('revistas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if titulo in row:
                return True
    return False

def escribir_csv(revista):
    with open('revistas.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(revista)

if __name__ == "__main__":
    os.system('cls')
    revistas = []
    url = "https://www.scimagojr.com/journalrank.php"
    html = procesar_html(url)
    extraer_datos(html)