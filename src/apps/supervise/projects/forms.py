# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.forms import ModelForm, ValidationError, Select
from django.forms.models import modelformset_factory

from apps.supervise.projects.models import Project


class ProjectForm(ModelForm):

    """
    Returns a form to crete or edit a project. ProjectForm inherits all the
    fields from Project model.

    :rtype: HTML Form
    
    .. versionadded :: 2.0.1
    """
    class Meta:
        model = Project