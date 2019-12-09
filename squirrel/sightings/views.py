from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from map.models import squirrels
from .forms import SquirrelForm

def index(request):
    sightings=squirrels.objects.all()
    context={'sightings':sightings,} 
    return render(request,"sightings/index.html",context)

def stats(request):
    stats1=squirrels.objects.all().count()
    stats2=squirrels.objects.filter(Runs_from=True).count()
    stats3=squirrels.objects.filter(Climbing=True).count()
    stats4=squirrels.objects.filter(Primary_fur_color='Black').count()
    stats5=squirrels.objects.filter(Chasing=True).count()
    context={'stats1':stats1,'stats2':stats2,'stats3':stats3,'stats4':stats4,'stats5':stats5,}
    return render(request,'sightings/stats.html',context)

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
# updating user information
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

