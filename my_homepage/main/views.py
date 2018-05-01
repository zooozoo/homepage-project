from datetime import datetime, timezone, timedelta

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.forms import NewsSelectForm
from main.models import NewsTitle
from member.forms import LoginForm
from .utils import all_crawler_function


# Create your views here.
def index_page(request):
    if NewsTitle.objects.last() is None or timedelta(minutes=30) < datetime.now(
            timezone.utc) - NewsTitle.objects.last().created_time:
        NewsTitle.objects.all().delete()
        for pres, title, link in all_crawler_function():
            NewsTitle.objects.create(pres=pres, title=title, link=link)
    if request.user.is_authenticated:
        selected_news_objects = request.user.newsselectmodel.get_user_news_objects()
        news_select_form = NewsSelectForm(instance=request.user.newsselectmodel)
    else:
        selected_news_objects = NewsTitle.objects.all()
        news_select_form = NewsSelectForm()
    form = LoginForm()
    context = {
        'selected_news_objects': selected_news_objects, # index에 뉴스 타이틀 뽑아오는데에 사용
        'news_select_form': news_select_form, # news_select_section 에 check_box 뽑아오는데에 사용
        'form': form,
    }
    return render(request, 'main/index.html', context)


@login_required(login_url='/member/login')
def news_select(request):
    form = NewsSelectForm(request.POST, instance=request.user.newsselectmodel)
    if form.is_valid():
        form.save()
    return redirect('/')
