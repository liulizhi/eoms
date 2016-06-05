from django.conf.urls import patterns

import views

urlpatterns = patterns('bbs.views',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^$', 'dashboard'),
    (r'bbsdetail/(?P<bid>\d+)/$', 'bbs_detail'),
    (r'add_blog/$', 'add_blog', {"template_name": "add_blog.html"}),
    (r'add_blog_pro/$', 'add_blog_pro'),
    (r'manage_blog_list/$', 'manage_blog_list'),
    (r'delete_blog/(?P<bid>\d+)/$', 'delete_blog'),
    (r'search/$', 'search',  {"template_name": "bbs_search.html"}),
    (r'search_deal/$', 'search_deal'),

)
