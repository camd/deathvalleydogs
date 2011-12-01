from dvdjango.data.models import Dog, Rig, Trip, Hike, Writeup, Quote
from django.contrib import admin

#class TripAdmin(admin.ModelAdmin):
#	pass

admin.site.register(Dog)
admin.site.register(Rig)
admin.site.register(Trip)
admin.site.register(Hike)
admin.site.register(Writeup)
admin.site.register(Quote)
