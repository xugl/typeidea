# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from pprint import pprint as pp

from django.db import connection
from django.db.models import Q,F,Count,Sum
from django.contrib.auth.models import User
from django.test.utils import override_settings
from django.test import TestCase

from .models import Category

#在TestCase模式下 debug=False  但是connection.querise必须设置debug=True,可以加个装饰器


class TestCategory(TestCase):
    @override_settings(DEBUG=True)
    def setUp(self):
        user = self.user = User.objects.create_user('the5fire','fake@email.com','password')

        Category.objects.bulk_create([
            Category(name='cate_buck_%s' % i ,owner=user)
            for i in range(10)
        ])
        #pp(connection.queries)

    @override_settings(DEBUG=True)
    def test_filter(self):
        categories = Category.objects.filter(
            (Q(id=1) & Q(id=2))
        )
        print(categories)


        print('===='*10)
        category = Category.objects.filter(id=1).update(status=F('status')+1)


        # users = User.objects.filter(username='the5fire').annotate(cate_count=Count('category'))
        user = User.objects.annotate(cate_count=Count('category')).get(username='the5fire')
        print(user.cate_count)

        user = User.objects.annotate(cate_count=Sum('category__status')).get(username='the5fire')
        print(user.cate_count)
        pp(connection.queries)

