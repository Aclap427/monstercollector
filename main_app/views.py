from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Monster:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

monsters = [
  Monster('Lolo', 'tabby', 'foul little demon', 3),
  Monster('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Monster('Raven', 'black tripod', '3 legged cat', 4)
]

def home(request):
    return HttpResponse('<h1>Welcome monsters</h1>')

def about(request):
    return render(request, 'about.html')

def monsters_index(request):
  return render(request, 'monsters/index.html', { 'monsters': monsters })