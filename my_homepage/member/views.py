from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from main.models import NewsSelectModel
from member.forms import LoginForm, SignUpForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('/')
    else:
        form = LoginForm()
    # 'login_page'는 login page의 nav에서 sideabar를 여는 버튼을 home link로 변경하기 위해
    # header 템플렛에 True를 전달하기 위한 것
    context = {
        'form': form,
        'login_page': True,
    }
    return render(request, 'member/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            NewsSelectModel.objects.create(user=user)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    context = {
        'form': form,
        'login_page': True,
    }
    return render(request, 'member/signup.html', context)
