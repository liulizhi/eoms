from django.conf.urls import patterns, include, url


urlpatterns = patterns('assets.views',

    url(r'^$', 'dashboard', {"template_name": "assets_list.html"}, name='dashboard'),
    url(r'^add$', 'add', {"template_name": "assets_add.html"}, name='add'),

)
