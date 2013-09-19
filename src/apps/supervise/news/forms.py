# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2013 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.forms import ModelForm, ValidationError, Select
from django.forms.models import modelformset_factory

from apps.supervise.news.models import Post

class PostForm(ModelForm):

    """
    Standard model for creating and editing a Post.

    :rtype: HTML form

    .. versionadded:: 2.0.1
    """
    class Meta:
        model = Post
