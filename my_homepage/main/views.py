from django.shortcuts import render
from .utils import naver_news_title, daum_news_title


# Create your views here.
def index_page(request):
    naver_news_list = naver_news_title()
    daum_news_list = daum_news_title()
    context = {
        'naver': naver_news_list,
        'daum': daum_news_list,
    }
    return render(request, 'main/index.html', context=context)
