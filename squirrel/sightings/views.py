from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm

def all_squirrels(request):
    squirrels=Squirrel.objects.all()[:45]
    context = {
        'squirrels':squirrels,
    }
    return render(request, 'sightings/all.html',context)

def update_squirrels(request, unique_squirrel_id):
     squirrel=Squirrel.objects.get(id=unique_squirrel_id)
     if request.method == 'POST':
         form=SquirrelForm(request.POST, instance=squirrel)
         
         if form.is_valid():
             form.save()
             return redirect(f'/sightings/{unique_squirrel_id}')
     else:
         form=SquirrelForm(instance=squirrel)
     context = {
         'form':form,
     }
     return render(request, 'sightings/update.html',context)

def add_squirrels(request):
    if request.method =='POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form=SquirrelForm()
    context ={
        'form':form,
    }
    return render(request, 'sightings/update.html',context)

def stats(request):
    total_number = Squirrel.objects.all().count()
    adult = Squirrel.objects.filter(age='Adult').count()
    juvenile = Squirrel.objects.filter(age='Juvenile').count()
    black = Squirrel.objects.filter(color='Black').count()
    cinnamon = Squirrel.objects.filter(color='Cinnamon').count()
    gray = Squirrel.objects.filter(color='Gray').count()
    running = Squirrel.objects.filter(running=True).count()
    chasing = Squirrel.objects.filter(chasing=True).count()
    climbing = Squirrel.objects.filter(climbing=True).count()
    eating = Squirrel.objects.filter(eating=True).count()
    foraging = Squirrel.objects.filter(foraging=True).count()
    context = {
        'total_numbel': total_number,
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


