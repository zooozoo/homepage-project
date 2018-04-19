from datetime import datetime, timezone, timedelta

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.forms import NewsSelectForm
from main.models import NaverNews, DaumNews, NewsSelectModel
from member.forms import LoginForm
from .utils import naver_news_title, daum_news_title


# Create your views here.
def index_page(request):
    if NaverNews.objects.last() is None or timedelta(minutes=15) < datetime.now(
            timezone.utc) - NaverNews.objects.last().created_time:
        NaverNews.objects.all().delete()
        DaumNews.objects.all().delete()
        naver_news_list = naver_news_title()
        daum_news_list = daum_news_title()
        for title, link in naver_news_list:
            NaverNews.objects.create(title=title, link=link)
        for title, link in daum_news_list:
            DaumNews.objects.create(title=title, link=link)
    news_select_form = NewsSelectForm()
    if request.user.is_authenticated:
        user_selected_news = request.user.newsselectmodel_set.first()
        data = {
            'naver': user_selected_news.naver,
            'daum': user_selected_news.daum,
        }
        news_select_form = NewsSelectForm(data, initial=data)
        if not news_select_form.is_valid():
            news_select_form = NewsSelectForm()
    naver = NaverNews.objects.all()
    daum = DaumNews.objects.all()
    form = LoginForm()
    context = {
        'naver': naver,
        'daum': daum,
        'form': form,
        'news_select_form': news_select_form
    }
    return render(request, 'main/index.html', context)
