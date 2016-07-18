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
PROJECT_DIR = os.path.split(os.path.abspath(__file__))[0]

def setup():
    global PODCASTS
    podcast_dir = os.path.join(PROJECT_DIR, "podcasts")
    print("PODCAST dir {}".format(podcast_dir))
    walker = os.walk(podcast_dir)
    for result in walker:
        print("IN ROW")
        for name in result[2]:
            if name.endswith("ttl"):
                filepath  = "{}/{}".format(result[0], name)
                print(filepath)
                PODCASTS.parse(filepath, format='turtle')
setup()
