from django.shortcuts import render_to_response, get_object_or_404
from dvdjango.data.models import Trip, Writeup
from django.template import RequestContext
# Create your views here.

def home(request):
    latest_writeups = Writeup.objects.all().order_by('created_at')[:5]
    #latest_photos = 
    return render_to_response('data/home.html', {'latest_writeups': latest_writeups},
                              context_instance=RequestContext(request))
