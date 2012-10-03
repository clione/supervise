# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

"""
URL definitions for the work groups, this URLs inherit the rest of the URL from
the main urls.py file.
"""

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

from apps.supervise.workgroups.views import ListWorkgroups, WorkgroupDetail, \
    DeleteWorkgroup, AddWorkgroup, EditWorkgroup

urlpatterns = patterns('',

    url(r'^$', ListWorkgroups.as_view(), name='workgroups_home'),

    url(r'^<(?P<groupid>[\w\-]+)/$', WorkgroupDetail.as_view(),
        name='workgroups_detail')

    url(r'^add/$', AddWorkgroup.as_view(), name='workgroups_add'),

    url(r'^edit/<(?P<groupid>[\w\-]+)/$', EditWorkgroup.as_view(),
        name='workgroups_edit'),

    url(r'^delete/<(?P<groupid>[\w\-]+)/$', DeleteWorkgroup.as_view(),
        name='workgroups_delete'),

)