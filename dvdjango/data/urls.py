from django.conf.urls.defaults import *

from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('dvdjango.data.views',
    (r'^home/$', 'home.home'),
    
    (r'^trips/$', 'trip.index'),
	(r'^trips/(?P<trip_id>\d+)/$', 'trip.detail'),
    
    (r'^dogs/$', 'dog.index'),
	(r'^dogs/(?P<dog_id>\d+)/$', 'dog.detail'),

)

