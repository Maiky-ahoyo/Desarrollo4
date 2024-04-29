from flask import Flask, render_template
from funciones import procesa_csv
from funciones import crea_dict_areas
from funciones import crea_dict_categorias
from funciones import crea_dict_catalogos
from funciones import crea_dict_editoriales
from funciones import crea_diccionario_iniciales
from funciones import crea_diccionario_qs
from funciones import busqueda_palabra
from funciones import busqueda_rango_sjr

app = Flask(__name__)
archivo_revistas = "revistas50.csv"
revistas = procesa_csv(archivo_revistas)
areas = crea_dict_areas(revistas)
categorias = crea_dict_categorias(revistas)
catalogos = crea_dict_catalogos(revistas)
editoriales = crea_dict_editoriales(revistas)
iniciales = crea_diccionario_iniciales(revistas)
qs = crea_diccionario_qs(revistas)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)