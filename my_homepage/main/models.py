from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class NewsTitle(models.Model):
    pres = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        pres_name = str(self.pres)
        time = str(self.created_time)
        return pres_name + ' ' + time


class NewsSelectModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    naver = models.BooleanField(default=True)
    daum = models.BooleanField(default=True)
    chosun = models.BooleanField(default=True, verbose_name='조선일보')
    joongang = models.BooleanField(default=True, verbose_name='중앙일보')
    donga = models.BooleanField(default=True, verbose_name='동아일보')
    hani = models.BooleanField(default=True, verbose_name='한겨레')
    ohmy = models.BooleanField(default=True, verbose_name='오마이뉴스')
    khan = models.BooleanField(default=True, verbose_name='경향신문')
    kbs = models.BooleanField(default=True, verbose_name='kbs')
    sbs = models.BooleanField(default=True, verbose_name='sbs')
    mbc = models.BooleanField(default=True, verbose_name='mbc')

    def __str__(self):
        return f'{self.user}\'s news select list'
