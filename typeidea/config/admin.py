# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.utils.html import format_html
from django.core.urlresolvers import reverse

from .models import Link, SideBar

from typeidea.custom_site import custom_site
from typeidea.custom_admin import BaseOwnerAdmin

from adminforms import LinkAdminForm,SideBarAdminForm


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
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

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(LinkAdmin, self).save_model(request, obj, form, change)



@admin.register(SideBar,site=custom_site)
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

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(SideBarAdmin, self).save_model(request, obj, form, change)

