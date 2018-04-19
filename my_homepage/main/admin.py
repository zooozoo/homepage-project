from django.contrib import admin

# Register your models here.
from main.models import NaverNews, DaumNews, NewsSelectModel

admin.site.register(NaverNews)
admin.site.register(DaumNews)
admin.site.register(NewsSelectModel)
