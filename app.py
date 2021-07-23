from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    iframe_do_carrosel = 'https://www.youtube.com/embed/AJ0bepmCeFo'
    descricao_1 = "Descrição 1"
    descricao_2 = "Descrição 2"
    descricao_3 = "Descrição 3"
    return render_template(
        "index.html",
        iframe_do_carrosel=iframe_do_carrosel,
        descricao_1 = descricao_1,
        descricao_2 = descricao_2,
        descricao_3 = descricao_3,

    )
@app.route("/servicos/")
def servicos():
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
