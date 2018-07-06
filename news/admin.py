from django.contrib import admin

# Register your models here.
from news.models import NewsItem, Event, Comment

admin.site.register(NewsItem)
admin.site.register(Event)
admin.site.register(Comment)
