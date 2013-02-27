# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

"""
Administration file for the workgroups admin panel.
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from apps.supervise.workgroups.models import WorkGroup


class WorkGroupAdmin(admin.ModelAdmin):

    """
    This is the administration for the workgroups. take in mind that the
    pub_date and the mod_date fields are automatically filled, so the
    only relevant fields are users and author. The users field contains
    the users in the group.

    :list_display: name, description, pub_date, mod_date, author
    :search_fields: name, description

    .. versionadded:: 2.0.1
    """
    list_display = ('name', 'description', 'pub_date', 'mod_date', 'author')
    search_fields = ('name', 'description')

    fieldsets = [
        (_('Details'), {'fields':
            ['name', 'description']}),

        (_('Other'), {'fields':
            ['users', 'author']}),
    ]

    # This modification of the save_model method allows django to store
    # the author of the object automatically, even from the admin.
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
        obj.users.add(request.user)

admin.site.register(WorkGroup, WorkGroupAdmin)