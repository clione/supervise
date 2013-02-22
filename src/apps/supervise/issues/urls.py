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

    url(r'^/$', name='issue_list'),

    url(r'^add/$', name='issue_add'),

    url(r'^<(?P<issue_id>\d+)/$', name='issue_detail'),

    url(r'^<(?P<issue_id>\d+)/delete/$', name='issue_delete'),

    url(r'^<(?P<issue_id>\d+)/edit/$', name='issue_edit'),

)