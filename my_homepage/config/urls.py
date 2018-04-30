"""my_homepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import index_page, news_select
from member.views import login_view, logout_view, signup_view, change_user_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='main'),
    path('news-select', news_select, name='news-select'),
    path('member/login', login_view, name='login'),
    path('member/logout', logout_view, name='logout'),
    path('member/signup', signup_view, name='signup'),
    path('member/change-user-info', change_user_info, name='change-user-info'),
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# DEBUG True 에서는 자동으로 static url이 추가된다.
