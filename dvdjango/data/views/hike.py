from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from dvdjango.data.models import Hike, Writeup
# Create your views here.

def index(request):
    hike_list = Hike.objects.all().order_by('date')
    return render_to_response('data/hike_index.html', {'hike_list': hike_list},
                              context_instance=RequestContext(request))

def detail(request, hike_id):
    t = get_object_or_404(Hike, pk=hike_id)
    return render_to_response('data/hike_detail.html', {'hike': t},
                              context_instance=RequestContext(request))
