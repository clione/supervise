# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns('',

    url(r'^/$', name='project_list'),

    url(r'^add/$', name='project_add'),

    url(r'^<(?P<project_url>[\w\-]+)/$', name='project_detail'),

    url(r'^<(?P<project_url>[\w\-]+)/delete/$', name='project_delete'),

    url(r'^<(?P<project_url>[\w\-]+)/edit/$', name='project_edit'),

    url(r'^<(?P<project_url>[\w\-]+)/issues/$',
        include('apps.supervise.issues.urls')),

    url(r'^<(?P<project_url>[\w\-]+)/news/$',
        include('apps.supervise.news.urls')),

)