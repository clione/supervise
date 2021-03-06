# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2013 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager
from apps.supervise.workgroups.models import WorkGroup


class Project(models.Model):

    """
    Project class, this contains all the information about the project and the
    people that is working on it.

    ..versionadded:: 2.0.1
    """

    name = models.CharField(_('Title'), max_length=250)
    url = models.CharField(_('URL'), max_length=250)
    description = models.TextField(_('Description'), null=True, blank=True)
    icon = models.ImageField(_('Icon'), blank=True, null=True,
        upload_to='projects/logos')
    private = models.BooleanField(_('Private'))
    tags = TaggableManager()

    admins = models.ManyToManyField(User, related_name='project_admins')
    group = models.ForeignKey(WorkGroup)

    # Base modules
    mod_wiki = models.BooleanField(_('Wiki'))
    mod_news = models.BooleanField(_('News'))
    mod_vcs = models.BooleanField(_('VCS'))
    mod_docs = models.BooleanField(_('File repository'))
    mod_issues = models.BooleanField(_('Issues'))

    # Information of creation and modification
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ['name']
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('project_detail', (), {
           'project_url': self.url})


class Component(models.Model):

    """
    Data model that inherits from CommonInfo and stablishes the Components
    of a project.
    """
    name = models.CharField(_('Name'), max_length=250)
    description = models.TextField(_('Description'), blank=True, null=True)
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField(_('Date'), auto_now_add=True)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Component')
        verbose_name_plural = _('Components')
        get_latest_by = 'pub_date'
