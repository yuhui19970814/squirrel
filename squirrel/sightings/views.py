from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from map.models import squirrels
from .forms import SquirrelForm

def index(request):
    sightings=squirrels.objects.all()
    context={'sightings':sightings,} 
    return render(request,"sightings/index.html",context)


def add(request):
    if request.method=="POST":
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sightings:index')
    else:
        form=SquirrelForm()
    context={'form':form}
    return render(request,'sightings/add.html',context)


def update(request, Unique_Squirrel_ID):
    sighting = squirrels.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=="POST":
        form=SquirrelForm(request.POST,instance=sighting)
        if form.is_valid():
            form.save()
            return redirect('sightings:index')
    else:
        form=SquirrelForm(instance=sighting)
    context={'form':form}
    return render(request,'sightings/update.html',context)

def stats(request):
    total_number = squirrels.objects.all().count()
    adult = squirrels.objects.filter(Age='Adult').count()
    juvenile = squirrels.objects.filter(Age='Juvenile').count()
    black = squirrels.objects.filter(Color='Black').count()
    cinnamon = squirrels.objects.filter(Color='Cinnamon').count()
    gray = squirrels.objects.filter(Color='Gray').count()
    running = squirrels.objects.filter(Running=True).count()
    chasing = squirrels.objects.filter(Chasing=True).count()
    climbing = squirrels.objects.filter(Climbing=True).count()
    eating = squirrels.objects.filter(Eating=True).count()
    foraging = squirrels.objects.filter(Foraging=True).count()
    context = {
        'total number': total_number,
        'adult': adult,
        'juvenile': juvenile,
        'black': black,
        'cinnamon': cinnamon,
        'gray': gray,
        'running': running,
        'chasing':chasing,
        'climbing':climbing,
        'eating':eating,
        'foraging':foraging,
    }
    return render(request, 'sightings/stats.html', context)


