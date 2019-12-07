from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm
def all_squirrels(request):
    squirrels=Squirrel.objects.all()[:100]
    context = {
        'squirrels':squirrels,
    }
    return render(request, 'sightings/all.html',context)
def update_squirrels(request, unique_squirrel_id):
     squirrel=Squirrel.objects.get(id=unique_squirrel_id)
     if request.method == 'POST':
         form=SquirrelForm(request.POST, instance=squirrel)
         # correct????
         if form.is_valid():
             form.save()
             return redirect(f'/sighting/{unique_squirrel_id}')
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


