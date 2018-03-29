from django.shortcuts import render
from .utils import naver_news_title


# Create your views here.
def index_page(request):
    naver = naver_news_title()
    context = {
        'naver': naver
    }
    return render(request, 'main/index.html', context=context)
