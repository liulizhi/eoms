from django.conf.urls import patterns


urlpatterns = patterns('assets.views',

    (r'^$', 'dashboard', {"template_name": "assets_list.html"}),

)
