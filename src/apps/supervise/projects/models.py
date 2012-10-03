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

from apps.thirdparty.taggit.managers import TaggableManager


class Project(models.Model):

    """
    Project class, this contains all the information about the project and the
    people that is working on it.

    ..versionadded:: 2.0.1
    """

    name = models.CharField(_('Title'), max_length=250)
    url = models.CharField(_('URL'), max_length=250)
    description = models.TextField(_('Description'))
    icon = models.ImageField(_('Icon'))
    public = models.BooleanField(_('Public'))
    tags = TaggableManager()

    admins = models.ManyToManyField(User)
    group = models.ForeignKey(Group)

    # Base modules
    mod_wiki = models.BooleanField(_('Wiki'))
    mod_news = models.BooleanField(_('News'))
    mod_vcs = models.BooleanField(_('VCS'))
    mod_docs = models.BooleanField(_('File repository'))
    mod_issues = models.BooleanField(_('Issues'))

    # Information of creation and modification
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_add=True)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ['title']
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('project_index', (), {
           'project_url': self.url})