from django.contrib import admin
from .models import Monster, Rental, Extra

# Register your models here.
admin.site.register(Monster)
admin.site.register(Rental)
admin.site.register(Extra)