#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb 
import os
import sys

from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask import render_template, url_for
from flask_flatpages.utils import pygmented_markdown
from flask_flatpages.page import Page

from itertools import takewhile
import operator
import pypandoc
import re



def convert_org_to_html(text):
    md = pypandoc.convert_text(text, to="markdown_strict",
                               format='org'
                               # , extra_args=['']
    )
    # print(md)
    # import IPython; IPython.embed()
    # raise
    output = pygmented_markdown(md)
    return output


class FlatOrgPages(FlatPages):
    def _parse(self, content, path):
        """Parse a flatpage file, i.e. read and parse its meta data and body.
        :return: initialized :class:`Page` instance.
        """
        lines = iter(content.split('\n'))

        # Read lines until an empty line is encountered.
        meta = '\n'.join(takewhile(operator.methodcaller('strip'), lines))
        # Translate simple org header
        def to_lower(matchobj):
            return matchobj.group(1).lower()
        meta = re.sub('\#\+([A-Z_]+:)', to_lower, meta)  
        # The rest is the content. `lines` is an iterator so it continues
        # where `itertools.takewhile` left it.
        content = '\n'.join(lines)

        # Now we ready to get HTML renderer function
        html_renderer = self.config('html_renderer')

        # If function is not callable yet, import it
        if not callable(html_renderer):
            html_renderer = import_string(html_renderer)

        # Make able to pass custom arguments to renderer function
        html_renderer = self._smart_html_renderer(html_renderer)

        # Initialize and return Page instance
        return Page(path, meta, content, html_renderer)



class OrgPage(Page):
    """A class that could translate an org-mode header to have the same characterics as a Page object
    by redefining the meta method.
    """
    import yaml
    from werkzeug.utils import cached_property
    @cached_property
    def meta(self):
        """A dict of metadata parsed as Emacs Org from the header of the file.
        This redefines the normal meta function.
        """
        def org_header_load(_meta):
            text = zip(re.findall('\#\+([A-Z_]+)', _meta),
                       re.findall(': (.*?)\\r', _meta))
            return {x.lower(): y.strip() for x, y in text}
        meta = org_header_load(self._meta)
        if not meta:
            return {}
        if not isinstance(meta, dict):
            raise ValueError("Expected a dict in metadata for '{0}', got {1}".
                             format(self.path, type(meta).__name__))
        return meta

# Build the website
app = Flask(__name__)

app.config.from_pyfile('settings.py')

app.config['FLATPAGES_HTML_RENDERER'] = convert_org_to_html

# pages = OrgPages(app)
pages = FlatOrgPages(app)

# # Views
# @app.route('/')
# def home():
#     # raise
#     posts = [page for page in pages if 'date' in page.meta]
#     # Sort pages by date
#     sorted_posts = sorted(posts, reverse=True,
#         key=lambda page: page.meta['date'])
#     return render_template('index.html', pages=pages)

# Views
@app.route('/')
def home():
    return render_template('oneyb_bs.html'
                           ,title='Hello, my name is Brian Oney'
                           ,name='Brian Oney'
                           ,location='Zurich, Switzerland<br>8053'
                           ,cards='Projects'
                           ,profile_pic="img/app_photo.png"
                           ,personal_bit="Likes the outdoors, especially during wintertime..."
                           ,copyleft="Copyleft &copy; Brian Oney 2017"
                           ,pages=pages
    )

@app.route('/<path:path>/')
def page(path):
    # Path is the filename of a page, without the file extension
    page = pages.get_or_404(path)
    # raise
    return render_template('page.html', page=page)

if __name__ == '__main__' and "freeze" not in sys.argv:
    app.run(debug=True)


if __name__ == '__main__' and "freeze" in sys.argv:
    # Freezer for static website
    freezer = Freezer(app)
    freezer.freeze()

# pdb.set_trace()
# import IPython; IPython.embed()

