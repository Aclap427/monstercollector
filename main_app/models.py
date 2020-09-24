from django.db import models
from django.urls import reverse
from datetime import date

TIMEFRAME = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)

class Extra(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('extras_detail', kwargs={'pk': self.id})

class Monster(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    origin = models.CharField(max_length=200, null=True)
    age = models.IntegerField()
    extras = models.ManyToManyField(Extra)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('detail', kwargs={'monster_id': self.id})

def rental_for_today(self):
    return self.rental_set.filter(date=date.today()).count() >= len(TIMEFRAME)

class Rental(models.Model):
  date = models.DateField('rental date')
  timeframe = models.CharField(
    max_length=1,
    choices=TIMEFRAME,
    default=TIMEFRAME[0][0]
  )
  monster = models.ForeignKey(Monster, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_timeframe_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']