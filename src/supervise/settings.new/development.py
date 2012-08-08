# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

"""
This file contains the specific settings for a development environment. That
includes database and some specific development stuff.
"""
import defaults

# Registration mail settings. Please use a different mail server and account
# during development than in production.
#EMAIL_HOST = ""
#EMAIL_PORT=
#EMAIL_HOST_USER=""
#EMAIL_HOST_PASSWORD=""
#DEFAULT_FROM_EMAIL = ""

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'supervise/db/development.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-gb'

SECRET_KEY = '++gl)#8*pj)=83ai*2littk%d!c02k2#cxj@4nup&amp;6&amp;-5%60k6'
