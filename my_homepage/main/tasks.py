from config.celery import app
from main.models import NewsTitle


@app.task
def crawling():
    NewsTitle.objects.create(pres='asdf', title='asdf', link='asdf')