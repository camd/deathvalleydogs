from django.shortcuts import render_to_response, get_object_or_404
from dvdjango.data.models import Rig
from django.template import RequestContext
from datetime import date

def index(request):
    rig_list = Rig.objects.filter(active=True).order_by('name')
    return render_to_response('data/rig_index.html', {'rig_list': rig_list},
                              context_instance=RequestContext(request))

def detail(request, rig_id):
    r = get_object_or_404(Rig, pk=rig_id)
    return render_to_response('data/rig_detail.html', {'rig': r},
                              context_instance=RequestContext(request))

