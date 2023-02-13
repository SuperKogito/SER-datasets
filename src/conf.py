# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
from datetime import datetime

# -- Project information -----------------------------------------------------

project = '🧠 SuperKogito/SER-datasets'
copyright = "2020-%s, Ayoub Malek" % datetime.now().year
author = 'Ayoub Malek'
html_favicon = "_static/favicon_io/favicon.ico"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    #'sphinx_contributors',
    'crate.sphinx.csv',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "github_url": "https://github.com/superkogito/ser-datasets",
    "search_bar_text": "Search this site...",

    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-field.html", "navbar-icon-links"],

    "external_links": [
        {"name": "Home", "url": "https://superkogito.github.io/index.html"},
        {"name": "Projects", "url": "https://superkogito.github.io/projects.html"},
        {"name": "Blog", "url": "https://superkogito.github.io/blog.html"},
        {"name": "About Me", "url": "https://superkogito.github.io/about.html"}
    ],
}

html_sidebars = {
    "index.html": ["layout.html", "footer.html"],
    "**": [],
}


blog_baseurl = "https://superkogito.github.io"
blog_title = "SuperKogito"
blog_path = "blog"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    "css/custom.css",
    "css/tree_graph.css",
    "css/social_media_sharing.css",
    'https://cdn.datatables.net/1.10.23/css/jquery.dataTables.min.css',
]

html_js_files = [
    'https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js',
    'js/main.js',
]
