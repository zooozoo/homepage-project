from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from member.forms import LoginForm


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
    return render(request, 'member/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')
