from flask import Flask, render_template # type: ignore
from funciones import carga_csv, peliculas_mas_recientes
from funciones import crea_diccionario_peliculas
from funciones import crea_diccionario_genero
from funciones import crea_diccionario_anios
from funciones import crea_diccionario_iniciales

archivo_cartelera = 'cartelera_2024.csv'
app = Flask(__name__)
cartelera = carga_csv(archivo_cartelera)
diccionario_peliculas=crea_diccionario_peliculas(cartelera)
diccionario_generos = crea_diccionario_genero(cartelera)
diccionario_anios = crea_diccionario_anios(cartelera)
diccionario_iniciales = crea_diccionario_iniciales(cartelera)

@app.route("/")
def index():
    global cartelera
    lista_peliculas = peliculas_mas_recientes(cartelera)
    return render_template("index.html",lista=lista_peliculas)

@app.route("/generos")
def generos():
    return render_template("generos.html",dicc_generos=diccionario_generos)

@app.route("/genero/<genero>")
def genero(genero:str):
    if genero in diccionario_generos:
        lista_peliculas = diccionario_generos[genero]
        return render_template("genero.html",lista_peliculas=lista_peliculas,genero=genero)
    else:
        return render_template("no_existe.html")  

@app.route("/anios")
def anios():
    return render_template("anios.html", dicc_anio=diccionario_anios)
    
@app.route("/anios/<anio>")
def anio(anio:str):
    if anio in diccionario_anios:
        lista_peliculas = diccionario_anios[anio]
        return render_template("anio.html",lista_peliculas=lista_peliculas,anio=anio)
    else:
        return render_template("no_existe.html")

@app.route("/alfabetico")
def alfabetico():
    return render_template("alfabetico.html", dicc_iniciales=diccionario_iniciales)
    
@app.route("/alfabetico/<inicial>")
def inicial(inicial:str):
    if inicial in diccionario_iniciales:
        lista_peliculas = diccionario_iniciales[inicial]
        return render_template("inicial.html",lista_peliculas=lista_peliculas,inicial=inicial)
    else:
        return render_template("no_existe.html")

@app.route("/pelicula/<id>")
def pelicula(id:str):
    if id in diccionario_peliculas:
        pelicula = diccionario_peliculas[id]  
        print(f"movie={pelicula['titulo']}")  
        return render_template("pelicula.html",movie=pelicula)
    else:
        return render_template("no_existe.html")
    
if __name__ == "__main__":
    app.run(debug=True)