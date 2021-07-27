from flask import Flask,render_template
from collections import namedtuple

app = Flask(__name__)

@app.route("/")
def index():
    iframe_do_carrosel = 'https://www.youtube.com/embed/AJ0bepmCeFo?&autoplay=1'

    return render_template(
        "index.html",iframe_do_carrosel=iframe_do_carrosel
    )
@app.route("/servicos/")
def servicos():

    # Card = namedtuple('Card', ['src_imagem', 'alt_descricao'])

    # codigo pra carregar json

    card = {
    "src_imagem":"link imagem",
    "alt_descricao":"descricao alt",
    "title":"tilte",
    "text":"text"
    }


    return render_template(
        "servicos.html"
    )
@app.route("/cover/")
def cover():
    return render_template(
        "cover.html"
    )
@app.route("/teste/<nome>/")
def teste(nome):
    return f'<h1>{nome}</h1>'


