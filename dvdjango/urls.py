from django.conf.urls.defaults import *
from django.views.static import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dvdjango/', include('dvdjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^info/', include('dvdjango.data.urls')),

	# Required to make static serving work
#	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
