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

from apps.supervise.projects.models import Project


class CreateProject(FormView):

    """
    """
    pass


class ViewProject(DetailView):

    """
    View the index page of a project.

    ..versionadded:: 2.0.1
    """

    context_object_name = 'project'
    template_name = 'projects/project_index.html'

    def get_object(self):
        project = get_object_or_404(Project,
            url = self.kwargs['project_title'])
        return project

    def get_context_data(self):
        context = super(ViewProject, self).get_context_data(**kwargs)
        project = self.kwargs['project_title']
        return context


class EditProject(UpdateView):

    """
    Edit current project raising a generic project form.

    :rtype: HTML form

    .. versionadded:: 2.0.1
    """
    model = Project
    template_name = 'projects/project_form.html'
    success_url = '/' #reverse('project_list')

    def get_object(self):
        prj = get_object_or_404(Project, url=self.kwargs['project_url'])
        return prj

    @method_decorator(permission_required('projects.edit_project'))
    def dispatch(self, *args, **kwargs):
        return super(EditProject)


class DeleteProject(DeleteView):

    """
    Deletes the current project and it's related content.

    .. versionadded:: 
    """
    context_object_name = 'project'
    success_url = '/' #reverse('project_list')

    def get_object(self):
        prj = get_object_or_404(Project, url=self.kwargs['project_url'])
        return prj

    @method_decorator(permission_required('projects.delete_project'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteProject, self).dispatch(*args, **kwargs)


class ListProjects(ListView):

    """
    List all the projects created in the platform.

    .. versionadded:: 2.0.1
    """
    paginate_by = 10
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ListProjects, self).get_context_data(**kwargs)
        return context