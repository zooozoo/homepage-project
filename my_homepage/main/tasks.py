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
    if latest_version > 2000:
        NewsTitle.objects.filter(version__lt=2001).delete()
        NewsTitle.objects.filter(version=latest_version).update(version=1)

    # try:
    #     latest_version = NewsTitle.objects.latest('version').version
    #     c = Crawling(latest_version + 1)
    #     NewsTitle.objects.bulk_create(c.all_crawler_collect())
    # except:
    #     c = Crawling(1)
    #     NewsTitle.objects.bulk_create(c.all_crawler_collect())


