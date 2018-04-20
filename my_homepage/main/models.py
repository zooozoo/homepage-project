from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Naver(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Daum(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class NewsSelectModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    naver = models.BooleanField(default=True)
    daum = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}\'s news select list'
