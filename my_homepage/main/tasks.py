from config.celery import app
from main.models import NewsTitle
from main.utils import Crawling


@app.task
def crawling():
    try:
        latest_version = NewsTitle.objects.latest('version').version
        c = Crawling(latest_version + 1)
        NewsTitle.objects.bulk_create(c.all_crawler_collect())
    except:
        latest_version = NewsTitle.objects.latest('version').version
        c = Crawling(latest_version + 1)
        NewsTitle.objects.bulk_create(c.all_crawler_collect())
    if latest_version > 1400:
        NewsTitle.objects.all().delte()

    # try:
    #     latest_version = NewsTitle.objects.latest('version').version
    #     c = Crawling(latest_version + 1)
    #     NewsTitle.objects.bulk_create(c.all_crawler_collect())
    # except:
    #     c = Crawling(1)
    #     NewsTitle.objects.bulk_create(c.all_crawler_collect())


