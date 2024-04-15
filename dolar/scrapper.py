'''
Web scrapper
'''
import os
import requests
from bs4 import BeautifulSoup
 
def scrap(URL:str):
    ''' Obtiene página desde Internet'''
    pagina = requests.get(URL)
    return pagina
 
def get_exchange_rate(dom):
    exchange_rates = {}
    for row in dom.find_all('p'):
        print(f"{row}")
        title = row.text.strip()
        if title[0] == 'C':
            title = 'Compra'
        elif title[0] == 'V':
            title = 'Venta'
        value = row.find('span')
        value = value.text.strip()
        exchange_rates[title] = value #actualizamos dict
    return exchange_rates
 
def get_max_min_exchange_rate(dict):
    lista_compra = []
    lista_venta = []
    lista_fix = []
    max_rate_compra_bank = ''
    max_rate_venta_bank = ''
    min_rate_compra_bank = ''
    min_rate_venta_bank = ''
    max_rate_fix_bank = ''
    min_rate_fix_bank = ''
    for k,v in dict.items():
        for key,value in v.items():
            if key == 'compra':
                lista_compra.append(value)
            if key == 'venta':
                lista_venta.append(value)
            if key == 'fix':
                lista_fix.append(value)    
    for k,v in dict.items():
        for key,value in v.items():
            if key == 'compra':
                if value == max(lista_compra):
                    max_rate_compra_bank = k
                if value == min(lista_compra):
                    min_rate_compra_bank = k
            if key == 'venta':
                if value == max(lista_venta):
                    max_rate_venta_bank = k
                if value == min(lista_venta):
                    min_rate_venta_bank = k
            if key == 'fix':
                if value == max(lista_fix):
                    max_rate_fix_bank = k
                if value == min(lista_fix):
                    min_rate_fix_bank = k        
    print(f"Mayor valor de compra: {max(lista_compra)} del banco {max_rate_compra_bank}")
    print(f"Mayor valor de venta: {max(lista_venta)} del banco {max_rate_venta_bank}")
    print(f"Mayor valor de fix: {max(lista_fix)} del banco {max_rate_fix_bank}")
    print(f"Menor valor de compra: {min(lista_compra)} del banco {min_rate_compra_bank}")
    print(f"Menor valor de venta: {min(lista_venta)} del banco {min_rate_venta_bank}")
    print(f"Menor valor de fix: {min(lista_fix)} del banco {min_rate_fix_bank}")
 
def get_exchange_rate_dict(dom):
    dictionary = {}
    body = dom.find('tbody')
    for row in body.find_all('tr'):
        columns = row.find_all('td')
        if (len(columns) == 4):
            update_with_4_columns(dictionary,columns)
        if (len(columns) == 5):
            update_with_5_columns(dictionary,columns)
    return dictionary
 
def update_with_4_columns(dictionary, columns):
    i = 0
    for col in columns:
        if i == 0:
            institucion = col.find(class_='small-hide').text.strip()
        if i == 3:
            fix = float(col.text.strip())
            d = {'fix':fix}
            dictionary[institucion] = d
        i+=1
 
def update_with_5_columns(dictionary, columns):
    i = 0
    for col in columns:
        if i == 0:
            institucion = col.find(class_='small-hide').text.strip()
        if i == 3:
            compra = float(col.text.strip())
        if i == 4:
            venta = float(col.text.strip())
            d = {'compra':compra,'venta':venta}
            dictionary[institucion] = d
        i+=1
 
def main():
    url = 'https://bit.ly/dolarInfo'
    pagina = scrap(url)
    soup = BeautifulSoup(pagina.content,"html.parser")
    table = soup.find(id='dllsTable')
    d = get_exchange_rate_dict(table)
    #imprimimos las instituciones y sus valores
    for k,v in d.items():
        print(k,v)
    #imprimimos el mayor y menor valor de compra y venta
    print("------------------------------------------------------------------------------------------")
    get_max_min_exchange_rate(d)
 
if __name__ == "__main__":
    os.system('cls')
    main()