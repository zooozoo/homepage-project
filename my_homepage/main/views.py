
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.forms import NewsSelectForm
from main.models import NewsTitle
from member.forms import LoginForm


# from .tasks import create_news_title_objects

# Create your views here.
def index_page(request):

    latest_version = NewsTitle.objects.latest('version').version
    news_title = NewsTitle.objects.filter(version=latest_version)
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
