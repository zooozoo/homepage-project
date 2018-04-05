from datetime import datetime, timezone, timedelta

from django.shortcuts import render

from main.models import NaverNews, DaumNews
from .utils import naver_news_title, daum_news_title


# Create your views here.
def index_page(request):
    if NaverNews.objects.last() is None or timedelta(minutes=15) < datetime.now(timezone.utc) - NaverNews.objects.last().created_time:
        NaverNews.objects.all().delete()
        DaumNews.objects.all().delete()
        naver_news_list = naver_news_title()
        daum_news_list = daum_news_title()
        print('new')
        for item in naver_news_list:
            NaverNews.objects.create(title=item)
        for item in daum_news_list:
            DaumNews.objects.create(title=item)
    naver = NaverNews.objects.all()
    daum = DaumNews.objects.all()
    context = {
        'naver': naver,
        'daum': daum,
    }
    return render(request, 'main/index.html', context=context)
