from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from dvdjango.data.models import Writeup
# Create your views here.

def detail(request, writeup_id):
    t = get_object_or_404(Writeup, pk=writeup_id)
    return render_to_response('data/writeup_detail.html', {'writeup': t},
                              context_instance=RequestContext(request))
