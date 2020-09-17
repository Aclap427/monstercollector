from django.db import models
from django.urls import reverse

# Create your models here.
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