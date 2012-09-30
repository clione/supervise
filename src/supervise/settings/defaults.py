# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

import os

####
# Django related stuff. Don't modify anthing in this section unless you know
# what you're doing.
####

# Activate the new url syntax in django 1.3 which will be
# compatible till 2.0
import django.template
django.template.add_to_builtins('django.templatetags.future')

# Get the current working directory
cwd = os.path.dirname(os.path.realpath(__file__)).strip('settings')

####
# END
####

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Public status of the site: 0 means private. 1 means public. Private will
# ask the users to login to enter. Default: 1
STATUS = 1

LANGUAGES = (
    ('en_GB', 'English'),
    ('es_ES', 'Español'),
    ('gl_ES', 'Galego')
)

# Userena settings. Please refer to the userena docs for help.
USERENA_SIGNIN_REDIRECT_URL = '/u/%(username)s/'
USERENA_ACTIVATION_DAYS = 7
USERENA_ACTIVATION_NOTIFY = True
USERENA_ACTIVATION_NOTIFY_DAYS = 2
USERENA_FORBIDDEN_USERNAMES = (
    'signup', 'signout', 'signin', 'activate', 'me', 'password', 'root',
    'admin', '1234', 'hacker'
)
USERENA_MUGSHOT_GRAVATAR = True
USERENA_MUGSHOT_DEFAULT = 'identicon'
USERENA_MUGSHOT_SIZE = 100
USERENA_MUGSHOT_PATH = 'mugshots/'
USERENA_DEFAULT_PRIVACY = 'registered'
# USERENA_LANGUAGE_FIELD = True

LOGIN_REDIRECT_URL = '/u/%(username)s/'
LOGIN_URL = '/u/signin/'
LOGOUT_URL = '/u/signout/'
ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = "accounts.UserProfile"

# Media and static directories and URLs settings
MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

AUTHENTICATION_BACKENDS = (
    'apps.thirdparty.userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.thirdparty.userena.middleware.UserenaLocaleMiddleware',
)

ROOT_URLCONF = 'supervise.urls'
WSGI_APPLICATION = 'supervise.wsgi.application'

TEMPLATE_DIRS = (
)

THIRDPARTY_APPS = (
    'apps.thirdparty.userena',
    'guardian',
    'easy_thumbnails',
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

SUPERVISE_APPS = (
    'core.accounts',
)

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + SUPERVISE_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
