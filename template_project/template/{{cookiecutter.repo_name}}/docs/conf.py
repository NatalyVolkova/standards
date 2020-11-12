#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Documentation build configuration file.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
import sys


extensions = [
    'sphinx.ext.autodoc',
    #'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']

source_suffix = ['.rst', '.md']

source_parsers = {
}

master_doc = 'index'

project = 'PROJECT NAME'
copyright = '2020, Gazprom Neft PSC'
author = 'Gazprom Neft'


# The full version, including alpha/beta/rc tags.
release = batchflow.__version__
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# choose html theme with custom css template
html_theme = 'sphinx_rtd_theme'


html_theme_options = {
}

html_static_path = ['_static']
def setup(app):
    app.add_stylesheet('custom.css')


autoclass_content = 'class'
add_module_names = False

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
    'pandas': ('http://pandas-docs.github.io/pandas-docs-travis/', None),
}
autodoc_mock_imports = ['torch']
viewcode_follow_imported_members = True

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'docs.tex', 'Documentation',
     author, 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, project, 'Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, project, 'Documentation',
     author, project, 'One line description of project.',
     'Miscellaneous'),
]
