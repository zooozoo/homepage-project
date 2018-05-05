from datetime import datetime, timezone, timedelta

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.forms import NewsSelectForm
from main.models import NewsTitle
from main.tasks import crawling
from member.forms import LoginForm
from .utils import all_crawler_collect


# from .tasks import create_news_title_objects

# Create your views here.
def index_page(request):
    # 뉴스객체 새로 만드는 함수 from tasks
    # transaction.on_commit(lambda: create_news_title_objects.delay())
    # if news_title.last() is None or timedelta(minutes=0.3) < datetime.now(
    #         timezone.utc) - news_title.last().created_time:
    news_title = NewsTitle.objects.filter(
        created_time__gte=datetime.now(timezone.utc) - timedelta(minutes=1)
    )
    # news_title = NewsTitle.objects.all()
    if request.user.is_authenticated:
        news_select_form = NewsSelectForm(instance=request.user.newsselectmodel)
    else:
        news_select_form = NewsSelectForm()
    form = LoginForm()
    context = {
        'news_title': news_title,  # 전체 언론사와 뉴스
        'news_select_form': news_select_form,  # user가 선택한 언론사의 이름 모음
        'form': form,
    }
    return render(request, 'main/index.html', context)


@login_required(login_url='/member/login')
def news_select(request):
    form = NewsSelectForm(request.POST, instance=request.user.newsselectmodel)
    if form.is_valid():
        form.save()
    return redirect('/')
