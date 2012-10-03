# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

from django.db import models
from django.contrib.auth.models import User


class WorkGroup(models.Model):

    """
    This class defines the data models for the dynamic work groups in the
    platform.

    .. versionadded:: 2.0.1
    """

    name = models.CharField(_('Name'), max_length=250)
    description = models.TextField(_('Description'), blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_add=True)
    author = models.ForeignKey(User, blank=True, null=True)
    users = models.ManyToManyField(User, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Workgroup')
        verbose_name_plural = _('Workgroups')
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('workgroups_detail', (), {
           'groupid': self.id})