# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.conf.urls import patterns, include, url

from apps.supervise.issues.views import AddTicket, EditTicket, DeleteTicket, \
    ListTickets, ViewTicket


urlpatterns = patterns('',

    url(r'^/$', ListTickets.as_view(), name='issue_list'),

    url(r'^add/$', AddTicket.as_view(), name='issue_add'),

    url(r'^<(?P<issue_id>\d+)/$', ViewTicket.as_view(), name='issue_detail'),

    url(r'^<(?P<issue_id>\d+)/delete/$', DeleteTicket.as_view(),
        name='issue_delete'),

    url(r'^<(?P<issue_id>\d+)/edit/$', EditTicket.as_view(),
        name='issue_edit'),

)