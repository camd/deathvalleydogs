from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('data.views',
	(r'^$', 'index'),
	(r'^(?P<trip_id>\d+)/$', 'detail'),
)

