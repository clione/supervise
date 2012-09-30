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