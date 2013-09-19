# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2013 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

from apps.supervise.news.views import CreatePost, EditPost, DeletePost, \
    ViewPost, ListPosts


urlpatterns = patterns('',

    url(r'^/$', ListPosts.as_view(), name='post_list'),

    url(r'^add/$', CreatePost.as_view(), name='post_add'),

    url(r'^<(?P<post_id>[\w\-]+)/$', ViewPost.as_view(), name='post_detail'),

    url(r'^<(?P<post_id>[\w\-]+)/delete/$', DeletePost.as_view(),
        name='post_delete'),

    url(r'^<(?P<post_id>[\w\-]+)/edit/$', EditPost.as_view(),
        name='post_edit'),

)
