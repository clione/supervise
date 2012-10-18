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


class ProjectAdmin(admin.ModelAdmin):

    """
    This is the project administration. pub_date and mod_date are automatically
    filled. Here goes all the information about the projects.

    :list_display: name, url, description, public, pub_date, author
    :search_fields: name, url, description

    .. versionadded:: 2.0.1 
    """
    list_display = ('name', 'url', 'description', 'public', 'pub_date',
                    'author')
    search_fields = ('name', 'url', 'description')

    fieldsets = [
        (_('Details'), {'fields':
            ['icon', ('name', 'url'), 'description', 'public', 'tags']}),

        (_('Users'), {'fields':
            ['admins', 'group']}),

        (_('Modules'), {'fields':
            ['mod_wiki', 'mod_news', 'mod_vcs', 'mod_issues', 'mod_docs']}),

        (_('Other'), {'fields':
            ['pub_date', 'mod_date', 'author']}), 
    ]

    # This modification of the save_model method allows django to store
    # the author of the object automatically, even from the admin.
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
        obj.users.add(request.user)