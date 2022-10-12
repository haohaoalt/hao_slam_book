# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os
import shlex
sys.path.insert(0, os.path.abspath('..'))
import recommonmark
from recommonmark.transform import AutoStructify


project = 'slam_docs'
copyright = '2022, Hao Zhang'
author = 'Hao Zhang'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = ['recommonmark'] 
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

# extensions = []


templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' 
html_static_path = ['_static']
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
app.add_transform(AutoStructify)
