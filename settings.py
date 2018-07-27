# -*- coding: utf-8 -*-


import os


def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))


# Assumes the app is located in the same directory where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))

REPO_NAME = os.path.basename(APP_DIR)  # Used for FREEZER_BASE_URL
DEBUG = True

# PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = APP_DIR
# Since this is a repo page (not a Github user page), we need to set the
# BASE_URL to the correct url as per GH Pages' standards

FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                    # will be deleted when you run the freezer

FLATPAGES_MARKDOWN_EXTENSIONS = []
FLATPAGES_ROOT = os.path.join(APP_DIR, 'content')
# print(FLATPAGES_ROOT) 
FLATPAGES_EXTENSION = '.org'
# FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
# FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
# FLATPAGES_EXTENSION = '.md'
