from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Monster, Extra
from .forms import RentalForm

class MonsterCreate(CreateView):
  model = Monster
  fields = ['name', 'breed', 'description', 'origin', 'age']
  success_url = '/monsters/'

class MonsterUpdate(UpdateView):
  model = Monster
  fields = ['breed', 'description', 'origin', 'age']
  success_url = '/monsters/'

class MonsterDelete(DeleteView):
  model = Monster
  success_url = '/monsters/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def monsters_index(request):
  monsters = Monster.objects.all()
  return render(request, 'monsters/index.html', { 'monsters': monsters })

def monsters_detail(request, monster_id):
  monster = Monster.objects.get(id=monster_id)
  extras_monster_doesnt_have = Extra.objects.exclude(id__in = monster.extras.all().values_list('id'))
  rental_form = RentalForm()
  return render(request, 'monsters/detail.html', {
    'monster': monster, 'rental_form': rental_form,
    'extras': extras_monster_doesnt_have
  })

def add_rental(request, monster_id):
  form = RentalForm(request.POST)
  if form.is_valid():
    new_rental = form.save(commit=False)
    new_rental.monster_id = monster_id
    new_rental.save()
  return redirect('detail', monster_id=monster_id)

def assoc_extra(request, monster_id, extra_id):
  Monster.objects.get(id=monster_id).extras.add(extra_id)
  return redirect('detail', monster_id=monster_id)

def unassoc_extra(request, monster_id, extra_id):
  Monster.objects.get(id=monster_id).extras.remove(extra_id)
  return redirect('detail', monster_id=monster_id)

class ExtraList(ListView):
  model = Extra
  fields = '__all__'

class ExtraDetail(DetailView):
  model = Extra
  fields = '__all__'

class ExtraCreate(CreateView):
  model = Extra
  fields = '__all__'

class ExtraUpdate(UpdateView):
  model = Extra
  fields = ['name','description']

class ExtraDelete(DeleteView):
  model = Extra
  success_url = '/extras/'