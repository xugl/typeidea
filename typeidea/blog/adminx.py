# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin

from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from .models import Post,Category,Tag

from typeidea.adminx import BaseOwnerAdmin
from .adminforms import  PostAdminForm,CategoryAdminForm,TagAdminForm

class PostAdmin(BaseOwnerAdmin):
    list_display = [
        'title','category','status_show','status','pv','uv',
        'owner','created_time','operator'
    ]
    #list_display_links = ['category', 'status']
    exclude =('html','owner','pv','uv')
    form = PostAdminForm
    list_filter = ['category']
    search_fields = ['title','category__name','owner__username']
    save_on_top = True
    show_full_result_count = False

    #补充
    actions_on_top = True
    actions_on_bottom = True

    date_hierarchy = 'created_time'
    #list_editable = ('title',)

    #编辑页面
    save_on_top = True
    #fields = (('title', 'category'),'content')   #两行
    #exclude =('owner',)   #不展示哪个字段
    fieldsets = (  # 跟fields互斥
        ('基础配置', {
            'fields': (
                ('category', 'title'),
                'desc',
                'status',
                ('content','is_markdown'),
            )
        }),
        ('高级配置', {
            'classes': ('collapse', 'addon'),  #展示高级配置选项
            'fields': ('tags',),
        }),
    )
    # form_layout = (
    #     Fieldset(
    #         "基础信息",
    #         'title',
    #         'desc',
    #         Row('category', 'status', 'is_markdown'),
    #         'content',
    #         'tags',
    #     ),
    # )

    filter_horizontal = ('tags',)    #多对多字段的管理  横向
    #filter_vertical = ('tags',)     #多对多字段的管理  竖向

    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change',args=(obj.id,))
            )
    #operator.allow_tags = True  #用format_html替代,django 1.9之后不建议使用
    operator.short_description = '操作'
    operator.empty_value_display = '???'

xadmin.site.register(Post,PostAdmin)


class PostInlineAdmin(admin.TabularInline):
    fields = ['title','status']
    extra = 1  # 控制额外多几个
    # min_num = 4
    # max_num = 4
    model = Post


class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [
    #     PostInlineAdmin
    # ]
    form = CategoryAdminForm
    list_display = [
        'name','status','status_show','is_nav',
        'owner','created_time','operator'
    ]
    list_filter = ['is_nav','created_time']
    search_fields = ['status','owner__username']
    actions_on_top = True
    actions_on_bottom = True
    show_full_result_count = False
    date_hierarchy = 'created_time'

    # 编辑页面
    save_on_top = True
    fieldsets = (  # 跟fields互斥
        ('基础配置', {
            'fields': (
                'name',
            )
        }),
        ('高级配置', {
            'classes': ('collapse', 'addon'),  # 展示高级配置选项
            'fields': (
                'is_nav',
                'status',
            )
        }),
    )

    def operator(self,obj):
        return format_html(
            '<a href="{}">删除</a>',
            reverse('cus_admin:blog_category_delete', args=(obj.id,))
            )
    operator.short_description = '操作'
    operator.empty_value_display = '???'

xadmin.site.register(Category,CategoryAdmin)


class TagAdmin(BaseOwnerAdmin):
    list_display = [
        'name','status','status_show','owner',
        'created_time','operator'
    ]
    form = TagAdminForm
    list_filter = ['created_time']
    search_fields = ['status','owner__username']
    actions_on_top = True
    actions_on_bottom = True
    show_full_result_count = False
    date_hierarchy = 'created_time'
    # 编辑页面
    save_on_top = True
    fieldsets = (  # 跟fields互斥
        ('基础配置', {
            'fields': (
                'name',
            )
        }),
        ('高级配置', {
            'classes': ('collapse', 'addon'),  # 展示高级配置选项
            'fields': (
                'status',
            )
        }),
    )

    def status_show(self,obj):
        return "当前状态: %s" % obj.status
    status_show.short_description = '状态展示'



    def operator(self,obj):
        return format_html(
            "<a href={}>删除</a>",
            reverse('cus_admin:blog_tag_delete', args=(obj.id,))
            )
    operator.short_description = '操作'
    operator.empty_value_display = '???'

xadmin.site.register(Tag,TagAdmin)