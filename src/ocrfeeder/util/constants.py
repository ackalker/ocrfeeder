# -*- coding: utf-8 -*-

###########################################################################
#    OCRFeeder - The complete OCR suite
#    Copyright (C) 2009 Joaquim Rocha
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################

import sys
import os
import locale

OCRFEEDER_STUDIO_NAME = 'OCRFeeder'
OCRFEEDER_COMPACT_NAME = 'ocrfeeder'
OCRFEEDER_STUDIO_VERSION = '0.7.1a'
OCRFEEDER_STUDIO_AUTHORS = ['Joaquim Rocha <joaquimrocha1@gmail.com>']
OCRFEEDER_STUDIO_ARTISTS = ['Joaquim Rocha <joaquimrocha1@gmail.com>']
OCRFEEDER_COPYRIGHT = 'Copyright © 2008-2010 Joaquim Rocha\n' \
                      'Copyright © 2009-2010 Igalia, SL'
OCRFEEDER_WEBSITE = 'http://live.gnome.org/OCRFeeder'
GPL_STATEMENT = """
    OCRFeeder is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OCRFeeder is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with OCRFeeder.  If not, see <http://www.gnu.org/licenses/>.
"""
OCRFEEDER_STUDIO_COMMENTS = 'The complete OCR suite.'

# DIRECTORIES
DEFAULT_SYSTEM_APP_DIR = os.path.join(sys.prefix, 'share', 'ocrfeeder')
APP_DIR = DEFAULT_SYSTEM_APP_DIR
RESOURCES_DIR = APP_DIR

# If the path does not exist (devel setup) set the
# APP_DIR and RESOURCES_DIR to local paths
if not os.path.exists(APP_DIR):
    APP_DIR = os.path.dirname(os.path.dirname(__file__))
    RESOURCES_DIR = os.path.join(APP_DIR, '../../resources')
RESOURCES_DIR = os.path.abspath(RESOURCES_DIR)

# I18N
DEFAULT_LANGUAGES = os.environ.get('LANGUAGE', '').split(':')
DEFAULT_LANGUAGES += ['en_US', 'pt_PT']
LOCALE_DIR = os.path.join(sys.prefix, 'share', 'locale')
OCRFEEDER_DEFAULT_LOCALE = locale.getdefaultlocale()[0]

# CUSTOM ICONS
DETECT_ICON = os.path.join(RESOURCES_DIR, 'icons', 'detect_icon.svg')
WINDOW_ICON = os.path.join(RESOURCES_DIR, 'icons', 'window_icon.png')
OCRFEEDER_ICON = os.path.join(RESOURCES_DIR, 'icons', 'ocr.svg')

#ENV VARIABLES
_OCRFEEDER_TEST_MODE = 'OCRFEEDER_TEST_MODE'
_OCRFEEDER_DEBUG_MODE = 'OCRFEEDER_DEBUG'

OCRFEEDER_ANGLE = False
if os.environ.get(_OCRFEEDER_TEST_MODE):
    OCRFEEDER_ANGLE = True

OCRFEEDER_DEBUG = False
if os.environ.get(_OCRFEEDER_DEBUG_MODE):
    OCRFEEDER_DEBUG = True

UNPAPER_COMMAND = 'unpaper'
GHOSTSCRIPT_COMMAND = 'gs'

# DeskTop Publishing Point (for calculating print measures)
DTP = 72
# location of glade spellchecker UI file

OCRFEEDER_SPELLCHECKER_UI = os.path.join(RESOURCES_DIR, 'spell-checker.ui')