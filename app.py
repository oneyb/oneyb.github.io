#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb 
import time
import sys

from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask import render_template, url_for
from flask_flatpages.page import Page

from flask_flatorgpages import convert_org_to_html, FlatOrgPages

# Build the website
app = Flask(__name__)

app.config.from_pyfile('settings.py')

app.config['FLATPAGES_HTML_RENDERER'] = convert_org_to_html

# pages = OrgPages(app)
pages = FlatOrgPages(app)


# Views
@app.route('/')
def home():
    return render_template('home.html'
                           ,title='Hello, my name is Brian Oney'
                           ,name='Brian Oney'
                           ,location='Rüschlikon, Switzerland<br>8803'
                           ,cards='Projects'
                           ,profile_pic="img/app_photo.png"
                           ,personal_bit="Likes the outdoors, especially during wintertime..."
                           ,personal_headline="Environmental Entrepreneur - Eternal Student"
                           ,copyleft="Copyleft &copy; Brian Oney 2016-%i" % time.localtime().tm_year
                           ,pages=pages
    )


@app.route('/<path:path>/')
def page(path):
    # Path is the filename of a page, without the file extension
    page = pages.get_or_404(path)
    # raise
    return render_template('page.html', page=page)


if __name__ == '__main__':
    if "freeze" in sys.argv:
        # Freezer for static website
        freezer = Freezer(app)
        freezer.freeze()
    else:
        app.run(debug=True)


# pdb.set_trace()
