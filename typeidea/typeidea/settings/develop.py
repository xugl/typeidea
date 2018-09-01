# coding:utf-8

from  .base import *   # noqa

DEBUG = True


ALLOWED_HOSTS = ['*']

# INSTALLED_APPS += [
#     'debug_toolbar',
# ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
