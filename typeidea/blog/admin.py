# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from .models import Post,Category,Tag


from typeidea.custom_site import custom_site


@admin.register(Post,site=custom_site)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','category','status_show','owner','created_time','operator']
    #list_display_links = ['category', 'status']

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
            'fields': (('category', 'title'), 'content')
        }),
        ('高级配置', {
            'classes': ('collapse', 'addon'),  #展示高级配置选项
            'fields': ('tags',),
        }),
    )
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



@admin.register(Category,site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag,site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass



#admin.site.register(Post,PostAdmin)
#admin.site.register(Category,CategoryAdmin)
#admin.site.register(Tag,TagAdmin)

