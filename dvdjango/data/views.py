from django.shortcuts import render_to_response, get_object_or_404
from data.models import Trip
# Create your views here.

def index(request):
    trip_list = Trip.objects.all().order_by('date')
    return render_to_response('data/index.html', {'trip_list': trip_list})

def detail(request, trip_id):
    t = get_object_or_404(Trip, pk=trip_id)
    return render_to_response('data/detail.html', {'trip': t})

