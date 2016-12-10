#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import os
import random
from utils import tag_from_text

app = Flask(__name__)
app.debug = True


def get_dinopix_image(text):
    resp = urllib2.urlopen('http://dinosaurpictures.org/api/dinosaur/random').read()
    obj = json.loads(resp)
    name = obj['name']
    url = 'http://dinosaurpictures.org/%s-pictures' % name
    return '%s: %s' % (name, url)

@app.route('/', methods=['GET', 'POST'])
def return_dinopix_image():
    if request.method == 'POST':
        text = request.form['text']
        req = {'text': get_dinopix_image(text)}
        return jsonify(**req)
    elif request.method == 'GET':
        return get_dinopix_image('')


if __name__ == '__main__':
    app.run()
