from flask import Flask, render_template, url_for
import itertools
from conteudo import (
    historia,
    aulas,
    oficinas,
    videos_lista
)

app = Flask(__name__)


@app.route("/")
def index():
    iframe_do_carrosel = "https://www.youtube.com/embed/AJ0bepmCeFo"
    banner2 = url_for("static", filename="imgs/banner2.jpg")
    banner1 = url_for("static", filename="imgs/banner1.jpg")
    # import pdb;pdb.set_trace()
    return render_template(
        "index.html",
        iframe_do_carrosel=iframe_do_carrosel,
        banner2=banner2,
        banner1=banner1,
        historia=historia,
    )


@app.route("/servicos/")
def servicos():
    cards = list(itertools.zip_longest(*[iter(oficinas)]*3,fillvalue="")) 
    # cards é uma lista de listas [ [card1,card2,card3],[card4,card5,card6],... ]
    return render_template("servicos2.html",aulas=aulas,cards=cards)

@app.route("/galeria/")
def galeria():

    import os
    lista_fotos = os.listdir('static/imgs/galeria')
    lista_fotos = list(itertools.zip_longest(*[iter(lista_fotos)]*4,fillvalue=""))

    return render_template("galeria.html",fotos=lista_fotos)


@app.route("/form_curso_example/")
def form_curso_example():
    return render_template("forms/curso.html")


@app.route("/videos/")
def videos():
    return render_template("videos.html",videos=videos_lista)


@app.route("/contato/")
def contato():
    return render_template("contat.html")
