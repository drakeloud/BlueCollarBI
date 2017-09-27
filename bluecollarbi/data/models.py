from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

import markdown

