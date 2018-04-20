from django.contrib import admin

# Register your models here.
from main.models import NewsTitle, NewsSelectModel

admin.site.register(NewsTitle)
admin.site.register(NewsSelectModel)
