# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Comment(models.Model):
     STATUS_ITEMS = (
          (1, '正常'),
          (2, '删除'),
     )
     target = models.CharField(max_length=200,null=True,verbose_name="评论目标")
     comment = models.CharField(max_length=2000,verbose_name="内容")
     nickname = models.CharField(max_length=50,verbose_name="昵称")
     website = models.URLField(verbose_name="网站")
     email = models.EmailField(verbose_name="邮箱")
     status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
     created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

     def __unicode__(self):
          return self.content

     def __str__(self):
          return self.content
     #owner = models.ForeignKey(User,verbose_name='用户')  不需要写，因为可以通过post 获取 user.
     class Meta:
         verbose_name = verbose_name_plural = "评论"