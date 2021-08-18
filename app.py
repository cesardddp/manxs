from flask import Flask, render_template, url_for
import itertools
from conteudo import (
    historia,
    aulas,
    aulas2,
    oficinas,
    videos_lista,
    cursos
)

app = Flask(__name__)


@app.route("/")
def index():
    iframe_do_carrosel = "https://www.youtube.com/embed/hlP-lESKS44"
    banner2 = url_for("static", filename="imgs/banner2.jpg")
    banner1 = url_for("static", filename="imgs/banner1.jpg")
    banner3 = url_for("static", filename="imgs/banner3.jpg")
    # import pdb;pdb.set_trace()
    return render_template(
        "index.html",
        iframe_do_carrosel=iframe_do_carrosel,
        banner2=banner2,
        banner1=banner1,
        banner3=banner3,
        historia=historia,

    )

    


@app.route("/servicos/")
def servicos():
    cards = list(itertools.zip_longest(*[iter(oficinas)]*3,fillvalue="")) 
    # cards é uma lista de listas [ [card1,card2,card3],[card4,card5,card6],... ]

    # import pdb; pdb.set_trace()

    return render_template("servicos2.html",aulas=aulas,aulas2=aulas2,cards=cards,cursos=cursos)


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
    return render_template("contato.html")

@app.route("/shows/")
def shows():
    return render_template("shows.html")

@app.route("/about/")
def about():      
    return render_template(
        "about.html",
        historia=historia,
        # banner=url_for("static", filename="imgs/WhatsApp Image 2021-08-04 at 09.37.51.jpeg")

    )

@app.route("/teste/")
def teste():
    return render_template("teste_aulas-servicos.html", aulas=aulas, aulas2=aulas2)