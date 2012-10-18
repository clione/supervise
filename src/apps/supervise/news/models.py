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


class Post(models.Model):

    """
    Post data model.

    .. version
    """
    title = models.CharField(_('Title'), max_length=250)
    body = models.TextField(_('Body'))
    tags = TaggableManager()

    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_add=True)
    author = models.ForeignKey(User)

    def name(self):
        return self.title

    def description(self):
        return self.body

    class Meta:
        ordering = ['title']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', (), {
           'project_url': self.url})