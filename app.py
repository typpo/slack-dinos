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


def get_dinopix_resp(text):
    resp = urllib2.urlopen('http://dinosaurpictures.org/api/dinosaur/random').read()
    obj = json.loads(resp)
    name = obj['name']
    url = 'http://dinosaurpictures.org/%s-pictures' % name
    return {
        'attachments': [
            {
                'text': '*<%s|%s>*' % (url, name),
                'image_url': obj['pics'][0]['url'],
            },
        ],
    }

@app.route('/', methods=['GET', 'POST'])
def return_dinopix_image():
    if request.method == 'POST':
        text = request.form['text']
        req = get_dinopix_resp(text)
        return jsonify(**req)
    elif request.method == 'GET':
        return jsonify(get_dinopix_resp(''))


if __name__ == '__main__':
    app.run()
