"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#####the5fire/the5fire@123456

from django.conf.urls import url
from blog.views import IndexView,CategoryView,TagView,PostView,AuthorView

import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()

from blog.api import PostViewSet,CategoryViewSet,TagViewSet,UserViewSet
from config.views import LinkView
from comment.views import CommentView
from typeidea import adminx  #NOQA
from .autocomplete import CategoryAutocomplete, TagAutocomplete

from ckeditor_uploader import urls as uploader_urls
from django.conf.urls import include
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
import re

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'tag', TagViewSet)
router.register(r'user', UserViewSet)


def static(prefix,**kwargs):
      return [
            url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')),serve,kwargs=kwargs),
      ]


urlpatterns = [
      url(r'^$', IndexView.as_view(), name='index'),
      url(r'^category/(?P<category_id>\d+)/$',CategoryView.as_view(), name='category'),
      url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
      url(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name='author'),
      url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name='detail'),
      url(r'^links/$', LinkView.as_view(), name='links'),
      url(r'^comment/$', CommentView.as_view(), name='comment'),
      url(r'^admin/', xadmin.site.urls),
      url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
      url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
      url(r'^api/docs/', include_docs_urls(title='typeidea api')),
      url(r'^api/', include(router.urls)),
  ] + uploader_urls.urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
      settings.STATIC_URL,document_root=settings.STATIC_ROOT
      )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
