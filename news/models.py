from django.db import models
from django.utils import timezone


# Create your models here.


class Base(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        abstract = True


class BaseNews(Base):
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Django_news/news/media/photos',
                              blank=True, null=True)

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


class Comment(models.Model):
    newItem = models.ForeignKey('NewsItem', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
