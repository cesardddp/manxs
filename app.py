from flask import Flask, render_template, url_for
from conteudo import ( historia, aulas, oficinas, videos_lista, cursos,
    redes_sociais_componente,biografia as bio
)
from flask_minify import minify, decorators

import json
import itertools
import os

RENDER_ID = False

app = Flask(__name__)

minify(app=app, passive=True)

from editor import editor_bp
app.register_blueprint(editor_bp)


@app.route("/")
@decorators.minify(html=True, js=True, cssless=True)
def index():
    iframe_do_carrosel = "https://www.youtube.com/embed/hlP-lESKS44"
    banner1 = url_for("static", filename="imgs/banner1.jpg")
    banner2 = url_for("static", filename="imgs/banner2.jpg")
    banner3 = url_for("static", filename="imgs/banner3.jpg")

    m_banner2 = url_for("static", filename="imgs/m_banner2.jpeg")
    m_banner1 = url_for("static", filename="imgs/m_banner1.jpeg")
    m_banner3 = url_for("static", filename="imgs/m_banner3.jpeg")

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
        render_id=RENDER_ID
    )


@app.route("/biografia/")
@decorators.minify(html=True, js=True, cssless=True)
def biografia():

    # biografia_data:dict = find_all("biografia")
    biografia_data:dict = bio

    return render_template(
        "biografia.html",
        redes_sociais_componente=redes_sociais_componente,
        biografia_data=biografia_data,
        render_id=RENDER_ID
    )


@app.route("/servicos/")
@decorators.minify(html=True, js=True, cssless=True)
def servicos():
    cards = list(itertools.zip_longest(*[iter(oficinas)] * 3, fillvalue=""))
    # cards é uma lista de listas [ [card1,card2,card3],[card4,card5,card6],... ]
    return render_template(
        "servicos.html", aulas=aulas, cards=cards, cursos=cursos, render_id=RENDER_ID    )


@app.route("/galeria/")
@decorators.minify(html=True, js=True, cssless=True)
def galeria():
    lista_fotos = sorted(os.listdir("static/imgs/galeria"))
    return render_template("galeria.html", fotos=set(lista_fotos), render_id=RENDER_ID)


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
    return render_template("forms/curso.html", estados=estados, render_id=RENDER_ID)


@app.route("/videos/")
@decorators.minify(html=True, js=True, cssless=True)
def videos():
    json.load(open("videos.json"))
    return render_template(
        "videos.html", videos=json.load(open("videos.json")), render_id=RENDER_ID    )


@app.route("/contato/")
@decorators.minify(html=True, js=True, cssless=True)
def contato():
    return render_template(
        "contato.html",
        redes_sociais_componente=redes_sociais_componente,
        render_id=RENDER_ID
    )


@app.route("/agenda/")
@decorators.minify(html=True, js=True, cssless=True)
def agenda():
    return render_template("agenda.html", render_id=RENDER_ID)


@app.route("/musicas/")
@decorators.minify(html=True, js=True, cssless=True)
def musicas():
    return render_template("musicas.html", render_id=RENDER_ID)


