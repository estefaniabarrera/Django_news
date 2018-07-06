from django import forms

from news.models import Comment
from .models import NewsItem, Event


class NewsForm(forms.ModelForm):
    publish_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = NewsItem
        fields = ('title', 'description', 'image', 'publish_date')


class EventForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Event
        fields = ('title', 'description', 'image', 'start_date', 'end_date')


# class EventSearchForm(forms.Form):
#     search_title = forms.CharField(
#         required=False,
#         label='Search title!',
#         widget=forms.TextInput(attrs={'placeholder': 'search here!'})
#     )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)