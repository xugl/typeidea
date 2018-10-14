# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment
from typeidea.custom_site import custom_site
from typeidea.custom_admin import BaseOwnerAdmin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from adminforms import  CommentAdminForm

@admin.register(Comment,site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = [
        'target','content','nickname','website',
        'email','created_timed_show','operator'
    ]
    form = CommentAdminForm
    actions_on_top = True
    actions_on_bottom = True
    show_full_result_count = True

    # 编辑页面
    save_on_top = True
    fields = (
        'target','content','nickname','website',
        'email',
    )

    def created_timed_show(self,obj):
        return "创建时间:%s" % obj.created_time.strftime('%Y-%m-%d')
    created_timed_show.short_description = "当前时间"

    def operator(self,obj):
        return format_html(
            "<a href='{}'>删除</a>",
            reverse("cus_admin:comment_comment_delete",args=(obj.id,))
        )
    operator.short_description = "操作"


