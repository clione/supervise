# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

"""
Administration file for the issues  admin panel.
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from apps.supervise.projects.models import Project, Component


class TicketAdmin(admin.ModelAdmin):

    """
    Administration for the tickets.
    """
    list_display = ('summary', 'description', 'status', 'project')
    search_fields = ('summary', 'description')
    fieldsets = [
        (_('Details'), {'fields':
            ['summary', 'description', ('status', 'ttype')]}),
        (_('Project details'), {'fields':
            [('project', 'component')]}),
        (_('Other'), {'fields':
            ['author', 'pub_date', 'last_mod', 'last_mod_author']}),
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
        obj.users.add(request.user)


class StatusAdmin(admin.ModelAdmin):

    """
    Administration model for the ticket status.

    .. versionadded:: 2.0.1
    """
    list_display = ('name', 'description', 'author')
    search_fields = ('name', 'description')
    fieldsets = [
        (_('Details'), {'fields':
            ['name', 'description', 'author', 'pub_date']})
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
        obj.users.add(request.user)


class TypeAdmin(admin.ModelAdmin):

    """
    Ticket types administration model.

    .. versionadded:: 2.0.1
    """
    list_display = ('name', 'description', 'author')
    search_fields = ('name', 'description')
    fieldsets = [
        (_('Details'), {'fields':
            ['name', 'description', 'author', 'pub_date']})
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
        obj.users.add(request.user)