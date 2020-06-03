from django.contrib import admin

from .models import Pasta, Salad, DinnerPlate

# Register your models here.
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlate)