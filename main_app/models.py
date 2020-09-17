from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

TIMEFRAME = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)
class Monster(models.Model):
    image = models.ImageField(upload_to='main_app/static/images', height_field=50, width_field=50, null=True)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    origin = models.CharField(max_length=200, null=True)
    age = models.IntegerField()

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
        return f"{self.get_timeframe_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
    