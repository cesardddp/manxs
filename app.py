from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    iframe_do_carrosel = 'https://www.youtube.com/embed/AJ0bepmCeFo?&autoplay=1'
    iframe_do_carrosel = 'https://www.youtube.com/embed/wD_Qu6qtx1g'

    return render_template(
        "index.html",iframe_do_carrosel=iframe_do_carrosel
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
