from datetime import timedelta, datetime, timezone

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from main.forms import NewsSelectForm
from main.models import NewsTitle
from main.utils import Crawling
from member.forms import LoginForm

from .tasks import crawling


# from .tasks import create_news_title_objects

# Create your views here.
def index_page(request):
    # if NewsTitle.objects.last() is None or timedelta(minutes=5) < datetime.now(
    #         timezone.utc) - NewsTitle.objects.last().created_time:
    #     crawling.delay()

    # latest version이 없을 경우 발생하는 에러를 잡기 위한 코드
    try:
        latest_version = NewsTitle.objects.latest('version').version
        news_title = NewsTitle.objects.filter(version=latest_version)
    except ObjectDoesNotExist:
        # 한번 더 요청하면 성공하는 경우를 대비해서 try문 중첩
        try:
            c = Crawling(1)
            NewsTitle.objects.bulk_create(c.all_crawler_collect())
            latest_version = NewsTitle.objects.latest('version').version
            news_title = NewsTitle.objects.filter(version=latest_version)
        except:
            c = Crawling(1)
            NewsTitle.objects.bulk_create(c.all_crawler_collect())
            latest_version = NewsTitle.objects.latest('version').version
            news_title = NewsTitle.objects.filter(version=latest_version)

    # latest_version = NewsTitle.objects.latest('version').version
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
