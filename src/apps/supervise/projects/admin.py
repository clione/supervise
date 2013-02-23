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

from apps.supervise.projects.models import Project, Component


class ComponentInline(admin.TabularInline):

    """
    This admin inline creates the component section inside the Project form.

    ..versionadded 2.0.1
    """
    model = Component


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

    inlines = [
        ComponentInline,
    ]

    # This modification of the save_model method allows django to store
    # the author of the object automatically, even from the admin.
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Project, ProjectAdmin)

# We leave this section of the admin commented since we already put the
# components part in a inline inside every project, which we think it's better
# for the end user.

# class ComponentAdmin(admin.modelAdmin):

#     """
#     Administration data model for the components around a project.

#     .. versionadded:: 2.0.1
#     """
#     list_display = ('name', 'description', 'project')
#     search_fields = ('name', 'description')
#     fieldsets = [
#         (_('Details'), {'fields':
#             ['name', 'description', 'project']}),
#     ]

#     # This modification of the save_model method allows django to store
#     # the author of the object automatically, even from the admin.
#     def save_model(self, request, obj, form, change):
#         if not change:
#             obj.author = request.user
#         obj.save()

#admin.site.register(Component, ComponentAdmin)