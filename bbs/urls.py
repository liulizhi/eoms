from django.conf.urls import patterns

import views

urlpatterns = patterns('bbs.views',
    (r'^$', 'index'),
    (r'(?P<bid>\d+)/details/$', 'bbs_detail'),
    #
    (r'(?P<bid>\d+)/edit/$', 'bbs_edit'),
    (r'(?P<bid>\d+)/update/$', 'update'),
    #
    (r'add/$', 'add_blog', {"template_name": "add_blog.html"}),
    (r'add_blog_pro/$', 'add_blog_pro'),
    (r'list/$', 'manage_blog_list'),
    (r'delete/(?P<bid>\d+)/$', 'delete_blog'),
    (r'search/$', 'search',  {"template_name": "bbs_search.html"}),
    (r'search_deal/$', 'search_deal'),

)
