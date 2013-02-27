# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.conf.urls import patterns, include, url

from apps.supervise.projects.views import ViewProject, EditProject, \
    DeleteProject, ListProjects, CreateProject


urlpatterns = patterns('',

    url(r'^/$', ListProjects.as_view(), name='project_list'),

    url(r'^add/$', CreateProject.as_view(), name='project_add'),

    url(r'^<(?P<project_url>[\w\-]+)/$', ViewProject.as_view(),
        name='project_detail'),

    url(r'^<(?P<project_url>[\w\-]+)/delete/$', DeleteProject.as_view(),
        name='project_delete'),

    url(r'^<(?P<project_url>[\w\-]+)/edit/$', EditProject.as_view(),
        name='project_edit'),

    url(r'^<(?P<project_url>[\w\-]+)/issues/$',
        include('apps.supervise.issues.urls')),

    url(r'^<(?P<project_url>[\w\-]+)/news/$',
        include('apps.supervise.news.urls')),

)