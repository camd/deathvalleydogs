from django.shortcuts import render_to_response, get_object_or_404
from dvdjango.data.models import Dog
from django.template import RequestContext
from datetime import date

def index(request):
    dog_list = Dog.objects.filter(active=True).order_by('name')
    return render_to_response('data/dog_index.html', {'dog_list': dog_list},
                              context_instance=RequestContext(request))

def detail(request, dog_id):
    d = get_object_or_404(Dog, pk=dog_id)
    return render_to_response('data/dog_detail.html', {'dog': d, 'age': age(d.birth_date)},
                              context_instance=RequestContext(request))

def age(from_date, leap_day_anniversary_Feb28=True):
    return date.today().year - from_date.year
