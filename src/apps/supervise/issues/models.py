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

from apps.supervise.projects.models import Project, Component


class CommonInfo(models.Model):

    """
    Abstract base class that contains common field between the extra infor for
    the tickets.

    .. versionadded: 2.0.1
    """

    # Programmers note:
    # For the Status and type to be defaults, we need a field that validates
    # only ONE object as the default, and prepopulates the field
    name = models.CharField(_('Name'))
    description = models.TextField(_('Description'), blank=True, null=True)
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField(_('Date'), auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']


class Status(CommonInfo):

    """
    This data model defines the possible statuses of the tickets in the
    platform.

    .. versionadded:: 2.0.1
    """
    class Meta(CommonInfo.Meta):
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')
        get_latest_by = 'pub_date'


class Type(CommonInfo):

    """
    Data model that defines the types of tickets, they can be for 
    enhancements, bugs, tasks, etc.

    .. versionadded:: 2.0.1
    """
    class Meta(CommonInfo.Meta):
        verbose_name = _('Type')
        verbose_name_plural = _('Types')
        get_latest_by = 'pub_date'


class Ticket(models.Model):

    """
    Issue ticket data model.

    .. versionadded:: 2.0.1
    """
    summary = models.CharField(_('Summary'), max_length=250)
    description = models.TextField(_('Description'))
    status = models.ForeignKey(Status)
    ttype = models.ForeignKey(Type)
    component = model.ForeignKey(Component, blank=True, null=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    owner = models.ForeignKey(User, blank=True, null=True)

    author = models.ForeignKey(User, blank=True, null=True)
    pub_date = models.DateTimeField(_('Date'), auto_now_add=True)
    last_mod = models.DateTimeField(_('Last update'), auto_now=True)
    last_mod_author = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.summary

    class Meta:
        ordering = ['summary']
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
        get_latest_by = 'pub_date'
