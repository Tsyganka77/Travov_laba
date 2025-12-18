# conf.py
import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'Сравнение удобства раскладок'
copyright = f'команда СВАЗЬ, 2025'
author = 'dima058n'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'myst_parser',  # если хотите использовать Markdown
]

# Поддержка Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ru'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_show_sphinx = False

# Добавление фавиконки
html_favicon = '_static/favicon.ico'

# -- Настройка темы RTD ------------------------------------------------------
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_nav': True,
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'logo_only': False,
}