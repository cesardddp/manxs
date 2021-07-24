from flask import Flask,render_template,url_for
from historia import historia

app = Flask(__name__)

@app.route("/")
def index():
    iframe_do_carrosel = 'https://www.youtube.com/embed/AJ0bepmCeFo'
    banner2 = url_for('static',filename='imgs/banner2.jpg')
    banner1 = url_for('static',filename='imgs/banner1.jpg')
    # import pdb;pdb.set_trace()
    return render_template(
        "index.html",
        iframe_do_carrosel=iframe_do_carrosel,
        banner2=banner2,
        banner1=banner1,
        historia=historia
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
