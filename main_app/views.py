from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Monster
from .forms import RentalForm


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
  rental_form = RentalForm()
  return render(request, 'monsters/detail.html', {
    'monster': monster, 'rental_form': rental_form
  })

class MonsterCreate(CreateView):
  model = Monster
  fields = ['name', 'breed', 'description', 'age']

class MonsterUpdate(UpdateView):
  model = Monster
  fields = ['breed', 'description', 'age']

class MonsterDelete(DeleteView):
  model = Monster
  success_url = '/monsters/index'

def add_rental(request, monster_id):
  form = RentalForm(request.POST)
  if form.is_valid():
    new_rental = form.save(commit=False)
    new_rental.monster_id = monster_id
    new_rental.save()
  return redirect('detail', monster_id=monster_id)