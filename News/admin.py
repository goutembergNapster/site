# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import Novidade, SportNews

admin.site.register(Novidade)
admin.site.register(SportNews)
