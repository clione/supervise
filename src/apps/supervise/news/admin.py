# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from apps.supervise.news.models import Post

class PostAdmin(admin.ModelAdmin):

    """
    Administration model for Post data model.

    .. versionadded:: 2.0.1
    """
    list_display = ('title', 'tags', 'author', 'project')
    search_fields = ('title', 'description', 'tags', 'author', 'project')
    fieldsets = [
        (_('Details'), {'fields':
            ['title', 'body', 'tags', 'project', 'author']})
    ]

    # This modification of the save_model method allows django to store
    # the author of the object automatically, even from the admin.
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
        obj.users.add(request.user)