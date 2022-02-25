from flask import Flask, render_template, url_for
from mongo import configure_app as mongo_config, find_all, load_data
from conteudo import ( historia, aulas, oficinas, videos_lista, cursos,
    redes_sociais_componente,
)
from config_dev import MONGO_URI
import itertools
import json
from flask_minify import minify, decorators

RENDER_ID = False

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI

mongo_config(app)

minify(app=app, passive=True)

from editor import editor_bp
app.register_blueprint(editor_bp)

# @app.before_first_request
# def first():
#     from mongo import delete_all,add_data
#     delete_all('biografia')
#     add_data()


# @freezer.register_generator
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
        render_id=RENDER_ID
    )


# @freezer.register_generator
@app.route("/biografia/")
@decorators.minify(html=True, js=True, cssless=True)
def biografia():

    biografia_data:dict = find_all("biografia")

    return render_template(
        "biografia.html",
        redes_sociais_componente=redes_sociais_componente,
        biografia_data=biografia_data,
        render_id=RENDER_ID
    )


# @freezer.register_generator
@app.route("/servicos/")
@decorators.minify(html=True, js=True, cssless=True)
def servicos():
    cards = list(itertools.zip_longest(*[iter(oficinas)] * 3, fillvalue=""))
    # cards é uma lista de listas [ [card1,card2,card3],[card4,card5,card6],... ]
    return render_template(
        "servicos.html", aulas=aulas, cards=cards, cursos=cursos, render_id=RENDER_ID    )


# @freezer.register_generator
@app.route("/galeria/")
@decorators.minify(html=True, js=True, cssless=True)
def galeria():

    import os

    lista_fotos = sorted(os.listdir("static/imgs/galeria"))

    lista_fotos = list(itertools.zip_longest(*[iter(lista_fotos)] * 3, fillvalue=""))
    # import ipdb;ipdb.set_trace()
    return render_template("galeria.html", fotos=set(lista_fotos), render_id=RENDER_ID)


# @freezer.register_generator
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


# @freezer.register_generator
@app.route("/videos/")
@decorators.minify(html=True, js=True, cssless=True)
def videos():
    json.load(open("videos.json"))
    return render_template(
        "videos.html", videos=json.load(open("videos.json")), render_id=RENDER_ID    )


# @freezer.register_generator
@app.route("/contato/")
@decorators.minify(html=True, js=True, cssless=True)
def contato():
    return render_template(
        "contato.html",
        redes_sociais_componente=redes_sociais_componente,
        render_id=RENDER_ID
    )


# @freezer.register_generator
@app.route("/shows/")
@decorators.minify(html=True, js=True, cssless=True)
def shows():
    return render_template("shows.html", render_id=RENDER_ID)


# @freezer.register_generator
@app.route("/musicas/")
@decorators.minify(html=True, js=True, cssless=True)
def musicas():
    return render_template("musicas.html", render_id=RENDER_ID)


# @app.route("/teste/")
# @decorators.minify(html=True, js=True, cssless=True)
# def teste():
#     return render_template("teste.html",
#     redes_sociais_componente=redes_sociais_componente,
#     render_id=RENDER_ID)