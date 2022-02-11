from flask import Flask, render_template, url_for
import itertools
from conteudo import ( historia, aulas, oficinas, videos_lista, cursos,
    redes_sociais_componente,
)
from data.biografia import (
    TITULO,
    BANNER,
    TEXTO_PRINCIPAL,
    FEITOS,
    TEXTO_HISTORICO,
    MUSICAS,
    TEXTO_FINAL,
    CARD_MISSAO,
    CARD_OBJETIVO,
    INSTAGRAMS
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
        render_id=False,
    )


@app.route("/biografia/")
@decorators.minify(html=True, js=True, cssless=True)
def biografia():

    titulo_data: dict = TITULO
    banner_data: dict = BANNER
    texto_principal_data: dict = TEXTO_PRINCIPAL
    feitos_data: dict = FEITOS
    texto_historico_data: dict = TEXTO_HISTORICO
    musicas_data: dict = MUSICAS
    texto_final_data: dict = TEXTO_FINAL
    card_missao_data: dict = CARD_MISSAO
    card_objetivo_data: dict = CARD_OBJETIVO
    instagrams_data:dict =INSTAGRAMS


    return render_template(
        "biografia.html",
        redes_sociais_componente=redes_sociais_componente,
        titulo_data=titulo_data,
        banner_data=banner_data,
        texto_principal_data=texto_principal_data,
        feitos_data=feitos_data,
        texto_historico_data=texto_historico_data,
        musicas_data=musicas_data,
        texto_final_data=texto_final_data,
        card_missao_data=card_missao_data,
        card_objetivo_data=card_objetivo_data,
        instagrams_data=instagrams_data,
        render_id=False,
    )


@app.route("/servicos/")
@decorators.minify(html=True, js=True, cssless=True)
def servicos():
    cards = list(itertools.zip_longest(*[iter(oficinas)] * 3, fillvalue=""))
    # cards é uma lista de listas [ [card1,card2,card3],[card4,card5,card6],... ]
    return render_template(
        "servicos.html", aulas=aulas, cards=cards, cursos=cursos, render_id=False
    )


@app.route("/galeria/")
@decorators.minify(html=True, js=True, cssless=True)
def galeria():

    import os

    lista_fotos = sorted(os.listdir("static/imgs/galeria"))

    lista_fotos = list(itertools.zip_longest(*[iter(lista_fotos)] * 3, fillvalue=""))
    # import ipdb;ipdb.set_trace()
    return render_template("galeria.html", fotos=set(lista_fotos), render_id=False)


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
    return render_template("forms/curso.html", estados=estados, render_id=False)


@app.route("/videos/")
@decorators.minify(html=True, js=True, cssless=True)
def videos():
    json.load(open("videos.json"))
    return render_template(
        "videos.html", videos=json.load(open("videos.json")), render_id=False
    )


@app.route("/contato/")
@decorators.minify(html=True, js=True, cssless=True)
def contato():
    return render_template(
        "contato.html",
        redes_sociais_componente=redes_sociais_componente,
        render_id=False,
    )


@app.route("/shows/")
@decorators.minify(html=True, js=True, cssless=True)
def shows():
    return render_template("shows.html", render_id=False)


@app.route("/musicas/")
@decorators.minify(html=True, js=True, cssless=True)
def musicas():
    return render_template("musicas.html", render_id=False)
