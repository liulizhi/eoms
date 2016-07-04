from django.conf.urls import include, url
from django.contrib import admin

#import bbs.urls
#import assets.urls
#import monitor.urls
#import configManage.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', 'bbs.views.dashboard', {"template_name": "dashboard.html"}),
]


# bbs message
urlpatterns += [
    url(r'^bbs/', include('bbs.urls')),
]

# config manage
urlpatterns += [
    url(r'^config/', include('configManage.urls')),
]

# assets message
urlpatterns += [
    url(r'^assets/', include('assets.urls', namespace='assets')),
]

# monitor message
urlpatterns += [
    url(r'^monitor/', include('monitor.urls')),
]


# author message
urlpatterns += [
    url(r'^author/$', 'bbs.views.author', {"template_name": "author_mess.html"}),
]

# user login
urlpatterns += [
    url(r'^login/$', 'bbs.views.bbs_login', {"template_name": "login.html"}),
    url(r'^auth/$', 'bbs.views.authen'),
    url(r'^logout/$', 'bbs.views.logout'),
    url(r'^userinfo/$', 'bbs.views.userinfo'),
    url(r'^setting/$', 'bbs.views.setting'),
    url(r'^account/$', 'bbs.views.account'),
]


