from deathvalleydogs.models import Trip, Writeup
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    latest_writeups = Writeup.objects.all().order_by('created_at')[:5]
    #latest_photos =
    return render_to_response('home.html', {'latest_writeups': latest_writeups},
                              context_instance=RequestContext(request))
