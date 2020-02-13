__author__ = "Jeremy Nelson"

import os
import rdflib
from flask import render_template
from .app import app, pages, PODCASTS


@app.route("/")
def home():
    podcats = []
    return render_template("index.html", pages=pages)

@app.route('/books/<path:title>/')
def moby_dick(title):
    if title.lower().startswith("moby-dick"):
        template = 'MobyDickOrtheWhalebyHermanMelville.html'
    elif title.lower().startswith("the-odyssey"):
        template = "TheOdysseybyHomer.html"
    return render_template(template)

@app.route("/<path:path>/")
def display(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)
