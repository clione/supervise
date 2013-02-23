# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.forms import ModelForm, ValidationError, Select

from apps.supervise.issues.models import Ticket, Status, Type


class TicketForm(ModelForm):

    """
    Returns a form to crete or edit a project. ProjectForm inherits all the
    fields from Project model.

    :rtype: HTML Form
    
    .. versionadded :: 2.0.1
    """
    class Meta:
        model = Ticket


class StatusForm(ModelForm):

    """
    Return a form to create or edit a status for the issues. Inherits all the
    fields from the Status data model.

    :rtype: HTML Form

    .. versionadded:: 2.0.1
    """
    class Meta:
        model = Status


class TypeForm(ModelForm):

    """
    Returns a form to create or edit issue types for the issues. Inherits all
    the fields from the Type data model.

    :rtype: HTML Form

    .. versionadded:: 2.0.1
    """
    class Meta:
        model = Type