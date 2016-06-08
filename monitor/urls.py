from django.conf.urls import patterns

import views

urlpatterns = patterns('monitor.views',

    (r'^$', 'dashboard', {"template_name": "mindex.html"}),


)
