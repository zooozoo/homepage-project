from datetime import datetime, timezone, timedelta

from django.shortcuts import render

from main.forms import NewsSelectForm
from main.models import NewsTitle
from member.forms import LoginForm
from .utils import naver_news_title, daum_news_title


# Create your views here.
def index_page(request):
    if NewsTitle.objects.last() is None or timedelta(minutes=15) < datetime.now(
            timezone.utc) - NewsTitle.objects.last().created_time:
        NewsTitle.objects.all().delete()
        for title, link in naver_news_title():
            NewsTitle.objects.create(pres='naver', title=title, link=link)
        for title, link in daum_news_title():
            NewsTitle.objects.create(pres='daum', title=title, link=link)
    if request.user.is_authenticated:
        user_selected_news = request.user.newsselectmodel
        selected_news_objects = request.user.newsselectmodel.get_user_news_objects()
        data = {
            'naver': user_selected_news.naver,
            'daum': user_selected_news.daum,
        }
        news_select_form = NewsSelectForm(data, initial=data)
    else:
        news_select_form = NewsSelectForm()
        selected_news_objects = NewsTitle.objects.all()
    form = LoginForm()
    context = {
        'selected_news_objects': selected_news_objects,
        'news_select_form': news_select_form,
        'form': form,
    }
    return render(request, 'main/index.html', context)
