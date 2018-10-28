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

from config.views import LinkView
from comment.views import CommentView
from typeidea import adminx  #NOQA


urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<tag_id>\d+)/$',TagView.as_view(),name='tag'),
    url(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^post/(?P<pk>\d+)/$',PostView.as_view() ,name='detail'),
    url(r'^links/$', LinkView.as_view(),name='links'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^admin/', xadmin.site.urls),
]