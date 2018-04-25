from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.elasticbeanstalk.com',
]

# local의 데이터베이스
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
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'