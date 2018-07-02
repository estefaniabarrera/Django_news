from django.contrib import admin

# Register your models here.
from news.models import NewsItem, Event

admin.site.register(NewsItem)
admin.site.register(Event)
