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

    url(r'^/$', name='post_list'),

    url(r'^add/$', name='post_add'),

    url(r'^<(?P<post_id>[\w\-]+)/$', name='post_detail'),

    url(r'^<(?P<post_id>[\w\-]+)/delete/$', name='post_delete'),

    url(r'^<(?P<post_id>[\w\-]+)/edit/$', name='post_edit'),

)