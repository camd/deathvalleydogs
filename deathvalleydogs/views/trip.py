from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from deathvalleydogs.models import Trip
# Create your views here.

def index(request):
    trip_list = Trip.objects.all().order_by('date')
    return render_to_response('trip_index.html', {'trip_list': trip_list},
                              context_instance=RequestContext(request))

def detail(request, trip_id):
    t = get_object_or_404(Trip, pk=trip_id)
    return render_to_response('trip_detail.html', {'trip': t},
                              context_instance=RequestContext(request))
