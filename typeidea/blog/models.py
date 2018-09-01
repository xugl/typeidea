# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
     STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
        (3, '草稿'),
     )
     title = models.CharField(max_length=50,blank=False,verbose_name="标题")  #blank=False 意思是form不能填空
     desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
     category = models.ForeignKey('Category',verbose_name="分类")
     tags = models.ManyToManyField('Tag',verbose_name="标签")
     status = models.IntegerField(default=1,choices=STATUS_ITEMS,verbose_name="状态")
     owner = models.ForeignKey(User,verbose_name="作者")
     created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")   #auto_now_add=True 每次增加记录时，赋予当前值
     #lasted_update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")  #auto_now=True 每次更新记录时，赋予当前值。
     content = models.TextField(verbose_name="内容",help_text="注: 正文必须为MarkDown格式")

     def __unicode__(self):
         return self.name

     class Meta:
         verbose_name = verbose_name_plural = "文章"

#post = Post.objects.all().defer('content')  --> select id,title from blog_post;
#post = Post.objects.all().only('title')     --> select title from blog_post;


class Category(models.Model):
     STATUS_ITEMS = (
         (1,'可用'),
         (2,'删除'),
     )
     name = models.CharField(max_length=50, verbose_name="名称")
     status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")  #PositiveIntegerField 正数
     is_nav = models.BooleanField(default=False, verbose_name="是否为导航")  #BooleanField 是否为布尔类型

     owner = models.ForeignKey(User, verbose_name="作者")
     created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

     def __unicode__(self):
         return self.name

     class Meta:
         verbose_name = verbose_name_plural = '分类'
         #ordering = ('id','created_time')
         #get_latest_by = ('id')

class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '标签'