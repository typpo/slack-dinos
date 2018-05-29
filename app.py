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
    while True:
        resp = urllib2.urlopen('http://dinosaurpictures.org/api/dinosaur/random').read()
        obj = json.loads(resp)
        name = obj['name']
        period = obj['period']
        eats = obj['eats']
        regions = ', '.join(obj['regions'])
        url = 'http://dinosaurpictures.org/%s-pictures' % name

        if not period or not eats or not regions or not obj['shouldShowMap']:
            continue

        return {
            'attachments': [
                {
                    'text': '*%s* lived in the %s and was a %s. It resided in %s.\n%s' \
                            % (name, period, eats, regions, url),
                    'image_url': obj['pics'][0]['url'],
                },
                {
                    'text': 'You can find %s here:' % (name),
                    'image_url': obj['mapUrl'],
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
