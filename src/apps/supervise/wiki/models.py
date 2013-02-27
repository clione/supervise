# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from apps.supervise.projects.models import Project


class Page(models.Model):

    """
    Wiki page data model.

    .. versionadded:: 2.0.1
    """
    name = models.CharField(_('Name'), max_length=250, primary_key=True)
    content = models.TextField(_('Content'), blank=True, null=True)
    project = models.ForeignKey(Project)
    version = models.IntegerField(_('Version'), blank=True, null=True)

    author = models.ForeignKey(User, blank=True, null=True,
        related_name='page_author')
    pub_date = models.DateTimeField(_('Date'), auto_now_add=True)
    last_mod = models.DateTimeField(_('Last update'), auto_now=True)
    last_mod_author = models.ForeignKey(User, blank=True, null=True,
        related_name='page_modified_author')

    class Meta:
        ordering = ['name']
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')
        get_latest_by = 'pub_date'

    @models.permalink
    def get_absolute_url(self):
        return ('page_detail', (), {
           'project_url': self.project.url,
           'pagename': self.name})