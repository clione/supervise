# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

"""
Main views file for the work groups, containing the add, edit, delete and
detail functions, as well as listing, etc.
"""

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from apps.supervise.workgroups.models import WorkGroup
from apps.supervise.workgroups.forms import WorkgroupForm


class ListWorkgroups(ListView):

    """
    List all the workgroups in the platform.

    .. versionadded:: 2.0.1
    """
    paginate_by = 10
    model = WorkGroup

    def get_context_data(self, **kwargs):
        context = super(ListWorkgroups, self).get_context_data(**kwargs)
        return context


class WorkgroupDetail(DetailView):

    """
    Show a list of the people inside a working group and the attached projects
    to it.

    .. versionadded:: 2.0.1
    """
    context_object_name = 'workgroup'
    template_name = 'workgroups/workgroup_detail.html'

    def get_object(self):
        wrkgrp = get_object_or_404(WorkGroup, id=self.kwargs['groupid'])
        return wrkgrp


class AddWorkgroup(FormView):

    """
    Create a new working group.

    .. versionadded:: 2.0.1
    """
    form_class = WorkgroupForm
    template_name = 'workgroups/workgroup_form.html'
    success_url = '/' #reverse('workgroups_home')

    def form_valid(self, form):
        wrkgrp = get_object_or_404(WorkGroup, id=self.kwargs['groupid'])
        form_uncommited = form.save(commit=False)
        form_uncommited.author = self.request.user
        form_uncommited.save()
        form.save_m2m()

        return super(AddWorkgroup, self).form_valid(form)

    @method_decorator(permission_required('workgroups.add_workgroup'))
    def dispatch(self, *args, **kwargs):
        return super(AddWorkgroup, self).dispatch(*args, **kwargs)


class EditWorkgroup(UpdateView):

    """
    """
    model = WorkGroup
    template_name = 'workgroups/workgroup_form.html'
    success_url = '/' #reverse('workgroups_home')

    def get_object(self):
        wrkgrp = get_object_or_404(WorkGroup, id=self.kwargs['groupid'])
        return wrkgrp

    @method_decorator(permission_required('workgroups.edit_workgroup'))
    def dispatch(self, *args, **kwargs):
        return super(EdittWorkgroup)


class DeleteWorkgroup(DeleteView):

    """
    """
    context_object_name = 'workgroup'
    success_url = '/' #reverse('workgroups_home')

    def get_object(self):
        wrkgrp = get_object_or_404(WorkGroup, id=self.kwargs['groupid'])
        return wrkgrp

    @method_decorator(permission_required('workgroups.delete_workgroup'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteWorkgroup, self).dispatch(*args, **kwargs)