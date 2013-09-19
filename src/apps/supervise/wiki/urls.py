# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2013 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.conf.urls import patterns, include, url
from django.utils.translation import ugettext_lazy as _

from apps.supervise.wiki.url_names import *


urlpatterns = patterns('',

    url(r'^/$', name='wiki_home'),

    url(r'^<(?P<pagename>\d+)/$', name=CHECK_PAGE),

    url(r'^<(?P<pagename>\d+)/add/$', name=ADD_PAGE),

    url(r'^<(?P<pagename>\d+)/delete/$', name=DELETE_PAGE),

    url(r'^<(?P<pagename>\d+)/edit/$', name=EDIT_PAGE),

)
