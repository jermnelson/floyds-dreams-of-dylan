"""
 Floyd's Dreams of Dylan

 Copyright 2012-2013 Jeremy Nelson, Floyd Shiery

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
__author__ = "Jeremy Nelson"

from bottle import template, request, route, run, static_file, HTTPError
import csv
import datetime
import json
import os 
APP_ROOT = os.path.abspath(".")

@route('/assets/<type_of:path>/<filename:path>')
def send_asset(type_of, filename):
    """
    Function returns static files from the assets directory but
    does not include music files from the podcast.
    
    :param type_of: Type of asset, choices are css, img, or js
    :param filename: file name of the asset
    """
    full_path = os.path.join(APP_ROOT,
                             "assets",
                             type_of,
                             filename)
    if os.path.exists(full_path):
        return static_file(filename,
			   root=os.path.join(APP_ROOT,
                                            "assets",
                                            type_of))

@route("/album/<name:path>")
def album(name):
    """
    Displays album information of songs used for Floyd's Dreams
    of Dylan.

    :param name: Name of Album
    """
    album_path = os.path.join(APP_ROOT,
                              "assets",
                              "js",
                              "{0}.json".format(name))
    if os.path.exists(album_path):
        album = json.load(open(album_path, 'rb'))
        return template('MusicAlbum', album=album)
    else:
        raise HTTPError(status="404", body="{0} not found".format(album_path))

@route("/dylans-head")
def head():
    """
    Displays description and inspiration of Dylan's Head
    """
    return template("dylans-head")

@route("/lucid-dreamer")
def head():
    """
    Displays Floyd as a lucid dreamer of the painting 
    """
    return template("lucid-dreamer")

@route("/podcasts/<name:path>")
def podcast(name):
    """
    Displays information about a podcast
    """
    return template(name)

@route("/title-island")
def head():
    """
    Displays description of Title Island
    """
    return template("title-island")


@route("/")
def home():
    """
    Displays the default view
    """
    return template("index")

run(host="localhost", port=8000)

