from flask import Flask, render_template, url_for
from funciones import procesa_csv
from funciones import crea_dict_areas
from funciones import crea_dict_categorias
from funciones import crea_dict_catalogos
from funciones import crea_dict_editoriales
from funciones import crea_dict_iniciales
from funciones import crea_dict_qs
from funciones import crea_lista_por_palabra
from funciones import crea_lista_palabras
from funciones import get_datos_revista
from funciones import paginacion

app = Flask(__name__)
archivo_revistas = "revistas.csv"
revistas = procesa_csv(archivo_revistas)
abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
total_paginas = len(revistas) // 50
areas_revistas = crea_dict_areas(revistas)
categorias_revistas = crea_dict_categorias(revistas)
catalogos_revistas = crea_dict_catalogos(revistas)
iniciales_revistas = crea_dict_iniciales(revistas)
qs_revistas = crea_dict_qs(revistas)
editoriales_revistas = crea_dict_editoriales(revistas)
qs = crea_dict_qs(revistas).keys()
catalogos = crea_dict_catalogos(revistas).keys()
editoriales = crea_dict_editoriales(revistas).keys()

@app.route("/")
def index():
    return render_template("index.html", alphabet=abecedario, qs=qs_revistas.keys(), catalogues=catalogos_revistas.keys())

@app.route("/magazines/<titulo>")
def magazine(titulo:str):   
    revista = get_datos_revista(revistas, titulo)[0]
    areas = get_datos_revista(revistas, titulo)[1]
    return render_template("magazine.html", magazine=revista, areas=areas)

@app.route("/magazines/page=<pagina>")
def magazines(pagina:str):
    ruta = "/magazines"
    pagina = int(pagina)
    total_revistas = len(revistas)
    revistas_paginadas = paginacion(revistas, pagina)
    primer_revista = ((pagina - 1) * 50) + 1
    ultima_revista = primer_revista + 49
    if ultima_revista > total_revistas:
        ultima_revista = total_revistas
    paginas_iniciales = [pagina, pagina+1, pagina+2]
    paginas_finales = [(len(revistas) // 50) - 1,(len(revistas) // 50),(len(revistas) // 50) + 1]
    if paginas_finales[0] < paginas_iniciales[0]:
        paginas_finales = [1, 1, 1]
    pagina_anterior = pagina - 1
    pagina_siguiente = pagina + 1
    return render_template("table.html", route=ruta, page=pagina, first_magazine=primer_revista, 
                           last_magazine=ultima_revista, first_pages=paginas_iniciales, 
                           last_pages=paginas_finales, total_magazines=total_revistas,
                           prev_page=pagina_anterior, next_page=pagina_siguiente, 
                           magazines=revistas_paginadas)

@app.route("/magazines/<sub>/page=<pagina>")
def catalogue(sub:str, pagina:str):
    for q in qs:
        if q in sub:
            revistas = qs_revistas[sub]
            texto = f"Magazines from the Q: {sub}"
    for catalogo in catalogos:
        if catalogo in sub:
            revistas = catalogos_revistas[sub]
            texto = f"Magazines from the catalogue: {sub}"
    for editorial in editoriales:
        if editorial in sub:
            revistas = editoriales_revistas[sub]
            texto = f"Magazines from the publisher: {sub}"        
    ruta = f"/magazines/{sub}"
    pagina = int(pagina)
    total_revistas = len(revistas)
    revistas_paginadas = paginacion(revistas, pagina)
    primer_revista = ((pagina - 1) * 50) + 1
    ultima_revista = primer_revista + 49
    if ultima_revista > total_revistas:
        ultima_revista = total_revistas
    paginas_iniciales = [pagina, pagina+1, pagina+2]
    paginas_finales = [(len(revistas) // 50) - 1,(len(revistas) // 50),(len(revistas) // 50) + 1]
    pagina_anterior = pagina - 1
    pagina_siguiente = pagina + 1
    return render_template("table.html", route=ruta, page=pagina, 
                           text=texto, first_magazine=primer_revista, 
                           last_magazine=ultima_revista, first_pages=paginas_iniciales, 
                           last_pages=paginas_finales, total_magazines=total_revistas,
                           prev_page=pagina_anterior, next_page=pagina_siguiente, 
                           magazines=revistas_paginadas)

@app.route("/areas")
def areas():
    return render_template("areas.html", areas=areas_revistas.keys())

@app.route("/areas/<area>/page=<pagina>")
def area(area:str, pagina:str):
    revistas = areas_revistas[area]
    texto = f"Magazines from the area: {area}"
    ruta = f"/areas/{area}"
    pagina = int(pagina)
    total_revistas = len(revistas)
    revistas_paginadas = paginacion(revistas, pagina)
    primer_revista = ((pagina - 1) * 50) + 1
    ultima_revista = primer_revista + 49
    if ultima_revista > total_revistas:
        ultima_revista = total_revistas
    paginas_iniciales = [pagina, pagina+1, pagina+2]
    paginas_finales = [(len(revistas) // 50) - 1,(len(revistas) // 50),(len(revistas) // 50) + 1]
    pagina_anterior = pagina - 1
    pagina_siguiente = pagina + 1
    return render_template("table.html", route=ruta, page=pagina, 
                           text=texto, first_magazine=primer_revista, 
                           last_magazine=ultima_revista, first_pages=paginas_iniciales, 
                           last_pages=paginas_finales, total_magazines=total_revistas,
                           prev_page=pagina_anterior, next_page=pagina_siguiente, 
                           magazines=revistas_paginadas)

@app.route("/categories")
def categories():
    return render_template("categories.html", categories=categorias_revistas.keys())

@app.route("/categories/<category>/page=<pagina>")
def category(category:str, pagina:str):
    revistas = categorias_revistas[category]
    texto = f"Magazines from the category: {category}"
    ruta = f"/categories/{category}"
    pagina = int(pagina)
    total_revistas = len(revistas)
    revistas_paginadas = paginacion(revistas, pagina)
    primer_revista = ((pagina - 1) * 50) + 1
    ultima_revista = primer_revista + 49
    if ultima_revista > total_revistas:
        ultima_revista = total_revistas
    paginas_iniciales = [pagina, pagina+1, pagina+2]
    paginas_finales = [(len(revistas) // 50) - 1,(len(revistas) // 50),(len(revistas) // 50) + 1]
    pagina_anterior = pagina - 1
    pagina_siguiente = pagina + 1
    return render_template("table.html", route=ruta, page=pagina, 
                           text=texto, first_magazine=primer_revista, 
                           last_magazine=ultima_revista, first_pages=paginas_iniciales, 
                           last_pages=paginas_finales, total_magazines=total_revistas,
                           prev_page=pagina_anterior, next_page=pagina_siguiente, 
                           magazines=revistas_paginadas)

@app.route("/initial/<initial>")
def initial(initial:str):
    return render_template("initial.html", initial=initial, keywords=crea_lista_palabras(revistas, initial))

@app.route("/initial/<initial>/<word>/page=<pagina>")
def word(initial:str, word:str, pagina:str):
    new_revistas = crea_lista_por_palabra(revistas, word)
    texto = f"Magazines containing the word: {word}"
    ruta = f"/initial/{initial}/{word}"
    pagina = int(pagina)
    total_revistas = len(new_revistas)
    revistas_paginadas = paginacion(new_revistas, pagina)
    primer_revista = ((pagina - 1) * 50) + 1
    ultima_revista = primer_revista + 49
    if ultima_revista > total_revistas:
        ultima_revista = total_revistas
    paginas_iniciales = [pagina, pagina+1, pagina+2]
    paginas_finales = [(len(new_revistas) // 50) - 1,(len(new_revistas) // 50),(len(new_revistas) // 50) + 1]
    pagina_anterior = pagina - 1
    pagina_siguiente = pagina + 1
    return render_template("table.html", route=ruta, page=pagina, 
                           text=texto, first_magazine=primer_revista, 
                           last_magazine=ultima_revista, first_pages=paginas_iniciales, 
                           last_pages=paginas_finales, total_magazines=total_revistas,
                           prev_page=pagina_anterior, next_page=pagina_siguiente, 
                           magazines=revistas_paginadas)
if __name__ == "__main__":
    app.run(debug=True)

    