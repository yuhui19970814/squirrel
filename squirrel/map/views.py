from django.shortcuts import render
# Create your views here


from .models import squirrels


def squirrels_map(request):
    sightings=squirrels.objects.all()[:45]
    
    return render(request, 'map/map.html',{'sightings':sightings})
# Create your views here.
