# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2013 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.core.urlresolvers import reverse
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

from apps.supervise.projects.models import Project
from apps.supervise.wiki.models import Page
from apps.supervise.wiki.forms import PageForm
from apps.supervise.wiki import url_names as urln


def check_page(request, project_url, pagename):

    """
    This view shows the wiki page if it exists or shows a page asking to
    create the page, which redirects to CreatePage class.

    .. versionadded:: 2.0.1
    """
    project = get_object_or_404(Project, url=project_url)

    try:
        wikipage = Page.objects.get(pk=pagename)
        return render_to_response('wiki/page_detail.html',
            {'wikipage': wikipage, 'project':project})

    except Page.DoesNotExist:
        return render_to_response('wiki/page_create.html',
            {'page_name': pagename, 'project':project})


class CreatePage(FormView):

    """
    This view shows a form to the user for creating a page in the wiki. We
    try at all moments to keep the user in the same URL.

    .. versionaddedd:: 2.0.1
    """
    form_class = PageForm
    template_name = 'wiki/page_form.html'

    def get_success_url(self):
        project = get_object_or_404(Project, url=self.kwargs['project_url'])
        wikipage = self.kwargs['page_name']
        return reverse(urln.CHECK_PAGE, kwargs={'project_url':project,
            'pagename':wikipage})

    def form_valid(self, form):

    def get_context_data(self, **kwargs):


class EditPage(UpdateView):

    """
    """
    pass


class DeletePage(FormView):

    """
    """
    pass
