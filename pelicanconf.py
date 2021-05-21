#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Mayank Suman'
SITEURL = 'https://mayanksuman.in'
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
HTTPS = True
SITENAME = f"{AUTHOR}'s Blog"
SITETITLE = AUTHOR
SITESUBTITLE = "Research Scholar, IIT Kharagpur"
SITEDESCRIPTION = f"{AUTHOR}'s Notes and Random Ideas"
SITELOGO = SITEURL + "/images/profile.png"
FAVICON = SITEURL + "/images/favicon.ico"

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TYPOGRIFY = True

# Blogroll
# LINKS = (('Contact', 'http://python.org/'),)

# Social widget
SOCIAL = (
    ('orcid', 'https://orcid.org/0000-0002-1402-8982'),
    ('github', 'https://github.com/mayanksuman'),
    ('stack-overflow', 'https://www.stackoverflow.com/users/8694152/ms'),
)

STATIC_PATHS = ['about/cv.pdf', 'images']

DEFAULT_PAGINATION = 5

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = AUTHOR

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Register jupyter notebook as additional markup format
MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup

IGNORE_FILES = [".ipynb_checkpoints"]

PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math', 'tipue_search', 'post_stats', 'better_figures_and_images', nb_markup]

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'authors', 'search')
ARTICLE_URL = 'posts/{date:%d}_{date:%b}_{date:%Y}_{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%d}_{date:%b}_{date:%Y}_{slug}/index.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': True},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

DISPLAY_CATEGORIES_ON_MENU = False

MAIN_MENU = True

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)
RENDER_MATHS = True
RESPONSIVE_IMAGES = True

THEME = "theme"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
