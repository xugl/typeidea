# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from pprint import pprint as pp

from django.db import connection
from django.contrib.auth.models import User
from django.test.utils import override_settings
from django.test import TestCase

from .models import Category

#在TestCase模式下 debug=False  但是connection.querise必须设置debug=True,可以加个装饰器


class TestCategory(TestCase):
    #@override_settings(DEBUG=True)
    def setUp(self):
        user = User.objects.create_user('the5fire','fake@email.com','password')
        for i in range(10):
            category_name = 'cate_%s' % i
            Category.objects.create(name=category_name,owner=user)

    @override_settings(DEBUG=True)
    def test_filter(self):
        categories = Category.objects.all()
        #print(len(categories))
        print(categories.count())
        categories = categories.filter(status=1)
        print(list(categories))
        print('--------')
        pp(connection.queries)
        print('---------')
        print(len(categories))

