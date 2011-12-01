from django.shortcuts import render_to_response, get_object_or_404
from dvdjango.data.models import Trip, Writeup
# Create your views here.

def t_index(request):
    trip_list = Trip.objects.all().order_by('date')
    return render_to_response('data/index.html', {'trip_list': trip_list})

def t_detail(request, trip_id):
    t = get_object_or_404(Trip, pk=trip_id)
    return render_to_response('data/detail.html', {'trip': t})

def x_home(request):
    latest_writeups = Writeup.objects.all().order_by('created_at')[:5]
    #latest_photos = 
    return render_to_response('data/home.html', {'latest_writeups': latest_writeups})
