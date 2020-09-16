from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Monster


# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def monsters_index(request):
  monsters = Monster.objects.all()
  return render(request, 'monsters/index.html', { 'monsters': monsters })

def monsters_detail(request, monster_id):
  monster = Monster.objects.get(id=monster_id)
  return render(request, 'monsters/detail.html', { 'monster': monster })

class MonsterCreate(CreateView):
  model = Monster
  fields = ['name', 'breed', 'description', 'age']

class MonsterUpdate(UpdateView):
  model = Monster
  fields = ['breed', 'description', 'age']

class MonsterDelete(DeleteView):
  model = Monster
  success_url = '/monsters/index'