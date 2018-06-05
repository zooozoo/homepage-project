import urllib.parse

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CELERY_BROKER_URL = 'amqp://localhost'


# AWS_ACCESS_KEY_ID = config_secret_common['aws']['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = config_secret_common['aws']['AWS_SECRET_ACCESS_KEY']
#
# aws_access_key_id = urllib.parse.quote(f'{AWS_ACCESS_KEY_ID}', safe='')
# aws_secret_access_key = urllib.parse.quote(f'{AWS_SECRET_ACCESS_KEY}', safe='')
#
# CELERY_BROKER_URL = f"sqs://{aws_access_key_id}:{aws_secret_access_key}@"

# CELERY_BEAT_SCHEDULE = {
#     'crawling': {
#         'task': 'main.tasks.crawling',
#         'schedule': 15.0
#     },
# }
