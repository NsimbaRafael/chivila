from app import app
from flask import render_template, url_for, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return redirect(url_for('index'))


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

@app.route("/localizacao")
def localizacao():
    return render_template("localizacao.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
