from flask import render_template
from .app import app, pages

@app.route("/")
def home():
    return render_template("index.html", pages=pages)

@app.route("/<path:path>/")
def display(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)
