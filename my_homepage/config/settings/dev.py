from .base import *

DEBUG = True

#local의 데이터베이스
DATABASES = config_secret_common["django"]["database-postgresql"]

CELERY_BROKER_URL = 'amqp://localhost'
