# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from news.models import Event, NewsItem

# Register your models here.


admin.site.register(NewsItem)
admin.site.register(Event)
