from .base import *
import urllib.parse

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.elasticbeanstalk.com',
    '.news-collecter.com',
]

DATABASES = config_secret_common["django"]["database-aws-rds"]

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

STATICFILES_STORAGE = 'config.storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

# S3 이용을 위한 AWS 정보
AWS_ACCESS_KEY_ID = config_secret_common['aws']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config_secret_common['aws']['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config_secret_common['aws']['AWS_STORAGE_BUCKET_NAME']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'
S3_USE_SIGV4 = True

# celery setting
aws_access_key_id = urllib.parse.quote(f'{AWS_ACCESS_KEY_ID}', safe='')
aws_secret_access_key = urllib.parse.quote(f'{AWS_SECRET_ACCESS_KEY}', safe='')

CELERY_BROKER_URL = f"sqs://{aws_access_key_id}:{aws_secret_access_key}@"
CELERY_RESULT_BACKEND = None # sqs는 celery backend를 지원하지 않는다.
CELERY_BEAT_SCHEDULE = {
    'crawling': {
        'task': 'main.tasks.crawling',
        'schedule': 300.0
    },
}
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# celery broker setting

# loadblancer health check 에러를 해결하기 위한 코드
import requests

EC2_PRIVATE_IP = None
try:
    EC2_PRIVATE_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout=0.01).text
except requests.exceptions.RequestException:
    pass

if EC2_PRIVATE_IP:
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)
