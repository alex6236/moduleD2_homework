# from django.shortcuts import render
# импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    template_name ='news.html'
    context_object_name = 'news'
    
class NewsDetail(DetailView):
    model = Post
    template_name ='news_id.html'
    context_object_name = 'news_id'