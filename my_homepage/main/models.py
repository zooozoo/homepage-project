from django.db import models


# Create your models here.
class NaverNews(models.Model):
    title = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)


class DaumNews(models.Model):
    title = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)
