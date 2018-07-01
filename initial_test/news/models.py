# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.db import models


# Create your models here.

class Base(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        abstract = True


class BaseNews(Base):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class NewsItem(BaseNews):
    publish_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Event(BaseNews):
    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=False)
