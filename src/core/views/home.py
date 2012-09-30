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
from django.contrib import messages
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.contrib.comments.models import Comment
from django.db.models import Count

from supervise.settings.defaults import STATUS
from apps.supervise.projects.models import Project
from apps.supervise.news.models import Post

def home(request):

	"""
	Returns the main site page. Depending on the status of the site it will
	show an overview of the projects or a login page in case it's private.

	.. versionadded:: 2.0.1

	:context: news, projects
	"""

	projects = Project.objects.all()
	news = Post.objects.all()

	if STATUS:
		return render_to_response('site_index.html',
								  {'projects': projects,
								   'news': news },
								  context_instance = RequestContext(request))
	else:
		return redirect('signin')