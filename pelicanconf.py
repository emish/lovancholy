#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'emish'
SITENAME = u'Lovancholy'
SITEURL = ''
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# The selected theme
THEME = 'wise-words-theme'

# Sets the date of articles to file stamp
DEFAULT_DATE = 'fs'
# The date format
DEFAULT_DATE_FORMAT = '%a %B %d, %Y'

TYPOGRIFY = True
DISPLAY_PAGES_ON_MENU = False
DIRECT_TEMPLATES = (('index', 'archives',))
STATIC_PATHS = ['images']


# Built-ins
###########

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
