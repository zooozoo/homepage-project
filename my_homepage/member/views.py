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
    context = {
        'form': form,
    }
    return render(request, 'member/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')
