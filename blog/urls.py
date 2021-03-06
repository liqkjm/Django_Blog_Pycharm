"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from blog import views
app_name = 'blog'
urlpatterns = [
    # path('^index$', )
    url(r'^$', views.index),
    url(r'^index.html$', views.index),
    url(r'^hnuer.html$', views.hnuer),
    url(r'^login.html$', views.login),
    url(r'^ykt_message.html', views.OneCard),
    url(r'^weichat_test$', views.weichat_test),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail')     # 博客详情页

]
