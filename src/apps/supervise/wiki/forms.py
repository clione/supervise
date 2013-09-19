# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2013 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.forms import ModelForm, ValidationError, Select

from apps.supervise.wiki.models import Page


class PageForm(ModelForm):

    """
    Returns a form to create a new wiki page.

    .. versionadded:: 2.0.1
    """
    class Meta:
        model = Page
