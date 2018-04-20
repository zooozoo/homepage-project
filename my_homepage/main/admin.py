from django.contrib import admin

# Register your models here.
from main.models import Naver, Daum, NewsSelectModel

admin.site.register(Naver)
admin.site.register(Daum)
admin.site.register(NewsSelectModel)
