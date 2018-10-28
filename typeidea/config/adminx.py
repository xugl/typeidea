# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.utils.html import format_html
from django.core.urlresolvers import reverse

from .models import Link, SideBar

import xadmin
from typeidea.adminx import BaseOwnerAdmin

from adminforms import LinkAdminForm,SideBarAdminForm


class LinkAdmin(object):
    form = LinkAdminForm
    actions_on_bottom = True
    actions_on_top = True
    save_on_top = True
    list_display = [
        'title', 'href', 'status', 'status_show',
        'weight', 'owner', 'created_time', 'operator',
    ]
    list_filter = [
        'owner__username',
        'href',
    ]
    search_fields = [
        'owner__username',
    ]

    fields = [
        'title', 'href', 'status',
        'weight',
    ]

    def status_show(self, obj):
        return '当前状态: %s' % obj.id

    status_show.short_description = "展示状态"

    def operator(self, obj):
        return format_html(
            "<a href={}>删除</a>",
            reverse("cus_admin:config_link_delete", args=(obj.id,))
        )

xadmin.site.register(Link, LinkAdmin)





class SideBarAdmin(BaseOwnerAdmin):
    actions_on_bottom = True
    actions_on_top = True
    save_on_top = True

    form = SideBarAdminForm

    list_display = [
        'title','display_type','content',
        'created_time','operator'

    ]

    fields = [
        'title', 'display_type', 'content',
    ]

    def operator(self, obj):
        return format_html(
            "<a href={}>删除</a>",
            reverse("cus_admin:config_sidebar_delete", args=(obj.id,))
        )
    operator.short_description = "操作"

xadmin.site.register(SideBar,SideBarAdmin)

