from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#      url(r'^$', 'deathvalleydogs.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
# )

urlpatterns = patterns(
    'deathvalleydogs.views',

    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'home.home'),
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

