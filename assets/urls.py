from django.conf.urls import patterns, url


urlpatterns = patterns('assets.views',

    url(r'^$', 'dashboard', {"template_name": "assets_list.html"}, name='dashboard'),
    url(r'^add/$', 'add', {"template_name": "assets_add.html"}, name='add'),
    url(r'^search/$', 'search', {"template_name": "search_assets_list.html"}, name='search'),

)
