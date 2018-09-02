# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Category,Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Post,PostAdmin)
#admin.site.register(Category,CategoryAdmin)
#admin.site.register(Tag,TagAdmin)

