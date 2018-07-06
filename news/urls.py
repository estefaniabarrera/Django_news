"""proyecto_formacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from news.views import NewsDetail, EventDetail, NewsUpdate, NewsAdd, NewsDelete, EventAdd, EventUpdate, \
    EventDelete
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all/$', views.all, name='all'),

    # EVENTS
    url(r'^events/$', views.event_list, name='events'),
    url(r'^events/(?P<pk>[0-9]+)/$', EventDetail.as_view(), name='detailEvent'),
    url(r'^events/add$', EventAdd.as_view(), name='addEvent'),
    url(r'^events/edit/(?P<pk>[0-9]+)/$', EventUpdate.as_view(), name='editEvent'),
    url(r'^events/delete/(?P<pk>[0-9]+)/$', EventDelete.as_view(), name='deleteEvent'),

    # NEWS

    # V1
    url(r'^news/v1/(?P<pk>[0-9]+)/$', NewsDetail.as_view(), name='v1DetailNews'),
    url(r'^news/v1/add$', views.news_add, name='v1NewsAdd'),
    url(r'^news/v1/(?P<pk>[0-9]+)/edit$', views.news_update, name='v1EditNews'),
    url(r'^news/v1/delete/(?P<pk>[0-9]+)/$', views.news_delete, name='v1DeleteNews'),

    # V2
    url(r'^news/$', views.news_list, name='news'),
    url(r'^news/v2/(?P<pk>[0-9]+)/$', NewsDetail.as_view(), name='detailNews'),
    url(r'^news/v2/(?P<pk>[0-9]+)/edit/$', NewsUpdate.as_view(), name='editNews'),
    url(r'^news/v2/add$', NewsAdd.as_view(), name='addNews'),
    url(r'^news/v2/delete/(?P<pk>[0-9]+)/$', NewsDelete.as_view(), name='deleteNews'),

    #SEARCH
    url(r'^search/$', views.search, name='search'),

    url(r'^news/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]
