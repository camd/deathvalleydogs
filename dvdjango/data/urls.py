from django.conf.urls.defaults import *

from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('dvdjango.data.views',
    (r'^home/$', 'home.home'),
	(r'^writeups/(?P<writeup_id>\d+)/$', 'writeup.detail'),
    
    (r'^trips/$', 'trip.index'),
	(r'^trips/(?P<trip_id>\d+)/$', 'trip.detail'),

    (r'^hikes/$', 'hike.index'),
	(r'^hikes/(?P<hike_id>\d+)/$', 'hike.detail'),
    
    (r'^dogs/$', 'dog.index'),
	(r'^dogs/(?P<dog_id>\d+)/$', 'dog.detail'),

    (r'^rigs/$', 'rig.index'),
	(r'^rigs/(?P<rig_id>\d+)/$', 'rig.detail'),


)

