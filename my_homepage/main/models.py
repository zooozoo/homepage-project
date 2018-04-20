from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class NewsTitle(models.Model):
    pres = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pres


class NewsSelectModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    naver = models.BooleanField(default=True)
    daum = models.BooleanField(default=True)

    def get_user_news_objects(self):
        fields_dict = dict(self.__dict__)
        picked_list = []
        for field, value in fields_dict.items():
            if value is True:
                picked_list.append(field)
        return NewsTitle.objects.filter(pres__in=picked_list)

    def __str__(self):
        return f'{self.user}\'s news select list'
