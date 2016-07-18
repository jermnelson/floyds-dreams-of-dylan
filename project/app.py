import os
import rdflib

from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

PODCASTS = rdflib.Graph()
PROJECT_DIR = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

def setup():
    global PODCASTS
    podcast_dir = os.path.join(PROJECT_DIR, "podcasts")
    walker = os.walk(podcast_dir)
    for result in walker:
        for name in result[2]:
            if name.endswith("ttl"):
                filepath  = "{}/{}".format(result[0], name)
                PODCASTS.parse(filepath, format='turtle')
setup()
