from datetime import timedelta, datetime, timezone

from config.celery import app
from main.models import NewsTitle
from main.utils import all_crawler_collect

@app.task
def create_news_title_objects():
    news_title = NewsTitle.objects.all()
    if news_title.last() is None or timedelta(minutes=0.3) < datetime.now(
            timezone.utc) - news_title.last().created_time:
        news_title.delete()
        for pres, title, link in all_crawler_collect():
            NewsTitle.objects.create(pres=pres, title=title, link=link)