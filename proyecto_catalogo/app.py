from flask import Flask, render_template
from funciones import procesa_csv
from funciones import crea_dict_areas
from funciones import crea_dict_categorias
from funciones import crea_dict_catalogos
from funciones import crea_dict_editoriales
from funciones import crea_diccionario_iniciales
from funciones import crea_diccionario_qs
from funciones import crea_dict_palabras_clave
from funciones import paginacion

app = Flask(__name__)
archivo_revistas = "revistas.csv"
revistas = procesa_csv(archivo_revistas)
abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
total_paginas = len(revistas) // 50
areas_revistas = crea_dict_areas(revistas)
categorias_revistas = crea_dict_categorias(revistas)
catalogos_revistas = crea_dict_catalogos(revistas)
editoriales_revistas = crea_dict_editoriales(revistas)
iniciales_revistas = crea_diccionario_iniciales(revistas)
qs_revistas = crea_diccionario_qs(revistas)

@app.route("/")
def index():
    return render_template("index.html", alphabet=abecedario, qs=qs_revistas.keys(), catalogues=catalogos_revistas.keys())

@app.route("/magazines/<pagina>")
def magazines(pagina:str):
    pagina = int(pagina)
    total_revistas = len(revistas)
    revistas_paginadas = paginacion(revistas, pagina)
    primer_revista = ((pagina - 1) * 50) + 1
    ultima_revista = primer_revista + 50
    if ultima_revista > total_revistas:
        ultima_revista = total_revistas
    paginas_iniciales = [pagina, pagina+1, pagina+2]
    paginas_finales = [(len(revistas) // 50) - 1,(len(revistas) // 50),(len(revistas) // 50) + 1]
    pagina_anterior = pagina - 1
    pagina_siguiente = pagina + 1
    return render_template("table.html", page=pagina, first_magazine=primer_revista, 
                           last_magazine=ultima_revista, first_pages=paginas_iniciales, 
                           last_pages=paginas_finales, total_magazines=total_revistas,
                           prev_page=pagina_anterior, next_page=pagina_siguiente, 
                           magazines=revistas_paginadas)

@app.route("/areas")
def areas():
    return render_template("areas.html", areas=areas_revistas.keys())

@app.route("/categories")
def categories():
    return render_template("categories.html", categories=categorias_revistas.keys())

@app.route("/initial/<inicial>")
def inicial(inicial:str):
    return render_template("inicial.html", initial=inicial, keywords=crea_dict_palabras_clave(revistas, inicial))

if __name__ == "__main__":
    app.run(debug=True)