# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from apps.supervise.projects.models import Project, Component
from apps.supervise.issues.models import Ticket, Status, Type


class ViewTicket(DetailView):

    """
    """
    pass


class AddTicket(FormView):

    """
    """
    pass


class EditTicket(UpdateView):

    """
    """
    pass


class DeleteTicket(DeleteView):

    """
    """
    pass


class ListTickets(ListView):

    """
    """
    pass