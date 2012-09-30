# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Clione Software
# Authors: Oscar Carballal Prego <oscar@clionesoftware.com>
# License: BSD Simplified (2-Clause BSD). See LICENSE for details.
#
# This file is part of Supervise project.

import defaults

DEBUG = True
TEMPLATE_DEBUG = DEBUG

__version__ = '2.0.0'
__status__ = 'alpha'

if DEBUG:
    from development import *
else:
    from production import *