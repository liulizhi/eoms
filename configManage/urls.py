from django.conf.urls import patterns


urlpatterns = patterns('configManage.views',

    (r'^$', 'dashboard', {"template_name": "config_dashboard.html"}),

)
