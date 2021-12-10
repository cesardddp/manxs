from flask import Flask, render_template, url_for, redirect
import itertools
from conteudo import historia, aulas, oficinas, videos_lista, cursos
from conteudo2 import (
    redes_sociais_componente,
    biografia as biografia_conteudo,
    instagrams,
)
import json
from flask_minify import minify, decorators


app = Flask(__name__)

minify(app=app, passive=True)


@app.route("/")
@decorators.minify(html=True, js=True, cssless=True)
def index():
    iframe_do_carrosel = "https://www.youtube.com/embed/hlP-lESKS44"
    banner2 = url_for("static", filename="imgs/banner2.jpg")
    banner1 = url_for("static", filename="imgs/banner1.jpg")
    banner3 = url_for("static", filename="imgs/banner3.jpg")

    m_banner2 = url_for("static", filename="imgs/m_banner2.jpeg")
    m_banner1 = url_for("static", filename="imgs/m_banner1.jpeg")
    m_banner3 = url_for("static", filename="imgs/m_banner3.jpeg")

    # import pdb;pdb.set_trace()
    return render_template(
        "index.html",
        iframe_do_carrosel=iframe_do_carrosel,
        banner2=banner2,
        banner1=banner1,
        banner3=banner3,
        m_banner2=m_banner2,
        m_banner1=m_banner1,
        m_banner3=m_banner3,
        historia=historia,
        redes_sociais_componente=redes_sociais_componente,
    )


@app.route("/biografia/")
@decorators.minify(html=True, js=True, cssless=True)
# @app.route("/biografia/")
def biografia():

    # import pdb;pdb.set_trace()
    return render_template(
        "biografia.html",
        historia=historia,
        redes_sociais_componente=redes_sociais_componente,
        biografia=biografia_conteudo,
        instagrams=instagrams,
    )


@app.route("/servicos/")
@decorators.minify(html=True, js=True, cssless=True)
def servicos():
    cards = list(itertools.zip_longest(*[iter(oficinas)] * 3, fillvalue=""))
    # cards é uma lista de listas [ [card1,card2,card3],[card4,card5,card6],... ]
    return render_template("servicos.html", aulas=aulas, cards=cards, cursos=cursos)


@app.route("/galeria/")
@decorators.minify(html=True, js=True, cssless=True)
def galeria():

    import os

    lista_fotos = sorted(os.listdir("static/imgs/galeria"))

    lista_fotos = list(itertools.zip_longest(*[iter(lista_fotos)] * 3, fillvalue=""))
    # import ipdb;ipdb.set_trace()
    return render_template("galeria.html", fotos=set(lista_fotos))


@app.route("/formulario/")
@decorators.minify(html=True, js=True, cssless=True)
def form_curso_example():
    estados = {
        "AC": "Acre",
        "AL": "Alagoas",
        "AP": "Amapá",
        "AM": "Amazonas",
        "BA": "Bahia",
        "CE": "Ceará",
        "DF": "Distrito Federal",
        "ES": "Espírito Santo",
        "GO": "Goiás",
        "MA": "Maranhão",
        "MT": "Mato Grosso",
        "MS": "Mato Grosso do Sul",
        "MG": "Minas Gerais",
        "PA": "Pará",
        "PB": "Paraíba",
        "PR": "Paraná",
        "PE": "Pernambuco",
        "PI": "Piauí",
        "RJ": "Rio de Janeiro",
        "RN": "Rio Grande do Norte",
        "RS": "Rio Grande do Sul",
        "RO": "Rondônia",
        "RR": "Roraima",
        "SC": "Santa Catarina",
        "SP": "São Paulo",
        "SE": "Sergipe",
        "TO": "Tocantins",
    }
    return render_template("forms/curso.html", estados=estados)


@app.route("/videos/")
@decorators.minify(html=True, js=True, cssless=True)
def videos():
    json.load(open("videos.json"))
    return render_template("videos.html", videos=json.load(open("videos.json")))


@app.route("/contato/")
@decorators.minify(html=True, js=True, cssless=True)
def contato():
    return render_template(
        "contato.html", redes_sociais_componente=redes_sociais_componente
    )


@app.route("/shows/")
@decorators.minify(html=True, js=True, cssless=True)
def shows():
    return render_template("shows.html")


@app.route("/musicas/")
@decorators.minify(html=True, js=True, cssless=True)
def musicas():
    return render_template("musicas.html")
