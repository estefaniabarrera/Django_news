from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from news.forms import NewsForm, EventForm
from news.models import NewsItem, Event

from search_views.search import SearchListView
from search_views.filters import BaseFilter


def index(request):
    return render(request, 'news/index.html', {})


def all(request):
    # import ipdb;
    # ipdb.set_trace()
    news = NewsItem.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    event = Event.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    paginator_news = Paginator(news, 2)
    paginator_events = Paginator(event, 10)
    page = request.GET.get('page')
    try:
        news = paginator_news.page(page)
        event = paginator_events.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator_news.page(1)
        event = paginator_events.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator_news.page(paginator_news.num_pages)
        event = paginator_events.page(paginator_events.num_pages)

    return render(request, 'news/list.html', {'NewsItem': news, 'Event': event})


def news_list(request):
    # import ipdb; ipdb.set_trace()
    news = NewsItem.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    paginator_news = Paginator(news, 2)
    page = request.GET.get('page')
    try:
        news = paginator_news.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator_news.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator_news.page(paginator_news.num_pages)

    return render(request, 'news/news_list.html', {'NewsItem': news})


def event_list(request):
    event = Event.objects.all().order_by('start_date')
    paginator_events = Paginator(event, 10)
    page = request.GET.get('page')
    try:
        event = paginator_events.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        event = paginator_events.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        event = paginator_events.page(paginator_events.num_pages)

    return render(request, 'news/event_list.html', {'Event': event})


# NEWS V1

def news_listv1(request, template_name='news/news_list.html'):
    # import ipdb; ipdb.set_trace()
    news = NewsItem.objects.all()
    data = {}
    data['object_list'] = news
    return render(request, template_name, data)


def news_add(request, template_name='news/news_form.html'):
    form = NewsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('news')
    return render(request, template_name, {'form': form})


def news_update(request, pk, template_name='news/news_form.html'):
    news = get_object_or_404(NewsItem, pk=pk)
    form = NewsForm(request.POST or None, instance=news)
    if form.is_valid():
        form.save()
        return redirect('news')
    return render(request, template_name, {'form': form})


def news_delete(request, pk, template_name='news/news_delete.html'):
    news = get_object_or_404(NewsItem, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news')
    return render(request, template_name, {'object': news})


# CLASS NEWS


class NewsAdd(CreateView):
    model = NewsItem
    success_url = reverse_lazy('addNews')
    form_class = NewsForm
    template_name = 'news/news_form.html'


class NewsUpdate(UpdateView):
    model = NewsItem
    success_url = reverse_lazy('editNews')
    fields = ['title', 'description', 'publish_date']
    template_name = 'news/news_form.html'


class NewsDelete(DeleteView):
    model = NewsItem
    success_url = reverse_lazy('deleteNews')
    template_name = 'news/news_delete.html'


class NewsDetail(DetailView):
    # import ipdb;
    # ipdb.set_trace()
    model = NewsItem
    template_name = 'news/news_detail.html'


# CLASS EVENT

class EventAdd(CreateView):
    model = Event
    success_url = reverse_lazy('addEvent')
    """fields = ['title', 'description', 'start_date', 'end_date']"""
    form_class = EventForm
    template_name = 'news/event_form.html'


class EventUpdate(UpdateView):
    model = Event
    success_url = reverse_lazy('editEvent')
    fields = ['title', 'description', 'start_date', 'end_date']
    template_name = 'news/event_form.html'


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('deleteEvent')
    template_name = 'news/event_delete.html'


class EventDetail(DetailView):
    model = Event
    template_name = 'news/event_detail.html'


#SEARCH
class NewsFilter(BaseFilter):
    search_fields = {
        'search_text' : ['name', 'surname'],
        'search_age_exact' : { 'operator' : '__exact', 'fields' : ['age'] },
        'search_age_min' : { 'operator' : '__gte', 'fields' : ['age'] },
        'search_age_max' : { 'operator' : '__lte', 'fields' : ['age'] },

    }

class ActorsSearchList(SearchListView):
    model = Actor
    paginate_by = 30
    template_name = "actors/actors_list.html"
    form_class = ActorSearchForm
    filter_class = ActorsFilter
