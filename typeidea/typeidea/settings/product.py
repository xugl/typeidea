# coding:utf-8

from  .base import *   # noqa

DEBUG = True


ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        # 'OPTIONS': {'charset': 'utf8mb4'}
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
    # 'raven.contrib.django.raven_compat',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
        'JQUERY_URL': '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js',
        'SHOW_COLLAPSED': True,
        'SHOW_TOOLBAR_CALLBACK': lambda x: True,
}

INTERNAL_IPS = ['192.168.28.141']


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PARSER_CLASS": "redis.connection.HiredisParser",
        }
    }
}