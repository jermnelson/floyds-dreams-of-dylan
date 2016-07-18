import os
import rdflib

from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

global PODCASTS

def setup():
    PODCASTS = rdflib.Graph()

    PROJECT_DIR = os.path.split(os.path.abspath(__file__))[0]
    walker = os.walk(os.path.join(PROJECT_DIR, "podcasts"))
    for result in walker:
        print("IN ROW")
        for name in result[2]:
            if name.endswith("ttl"):
                filepath  = "{}/{}".format(result[0], name)
                print(filepath)
                PODCASTS.parse(filepath, format='turtle')
setup()
