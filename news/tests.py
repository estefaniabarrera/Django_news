from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone

from news.forms import NewsForm
from news.models import NewsItem, Event


def news_add(title):
    time = timezone.now()
    return NewsItem.objects.create(title=title, description="test description", publish_date=time)


def event_add(title):
    time = timezone.now()
    return Event.objects.create(title=title, description="test description", start_date=time, end_date=time)


class NewsItemTest(TestCase):

    def test_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_new(self):
        resp = self.client.get(reverse('news'))
        self.assertEqual(resp.status_code, 200)

    def test_event(self):
        resp = self.client.get(reverse('events'))
        self.assertEqual(resp.status_code, 200)

    def test_all(self):
        resp = self.client.get(reverse('all'))
        self.assertEqual(resp.status_code, 200)

    def test_class_form(self):
        data = {'title': "title", 'description': "test description", 'publish_date': timezone.now()}
        form = NewsForm(data=data)
        form.save()
        self.assertTrue(form.is_valid())
        x = NewsItem.objects.get(title="title")
        self.assertTrue(x)

    def test_v2detail(self):
        w = news_add("test")
        resp = self.client.get(reverse('detailNews', kwargs={'pk': w.id}))
        self.assertEqual(resp.status_code, 200)
