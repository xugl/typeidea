#!/usr/bin/python
# coding:utf-8

from __future__ import unicode_literals
from __future__ import print_function

import xadmin
from xadmin.views import CommAdminView

class BaseOwnerAdmin(object):
    """ 针对有owner属性的数据，重写
    1,save_model -保证每条数据都属于当前用户
    2,重写get_queryset -保证每个用户只能看到自己的文章
    """

    def get_list_queryset(self):
        request = self.request
        qs = super(BaseOwnerAdmin, self).get_list_queryset()
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_models(self):
        if  self.org_obj:
            return super(BaseOwnerAdmin, self).save_models()

        self.new_obj.owner = self.request.user
        return super(BaseOwnerAdmin, self).save_models()


class GlobalSetting(CommAdminView):
    site_title = 'Typeidea管理后台'
    site_footer = 'power by the5fire.com'

    # def get_nav_menu(self):
    #     return [
    #         {
    #             'title': '随便吧',
    #             'url': 'http://the5fire.com',
    #             'icon': '',
    #             'perm': True,
    #             'order': 1,
    #         }
    #
    #     ]

xadmin.site.register(CommAdminView,GlobalSetting)