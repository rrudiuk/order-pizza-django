from django.contrib import admin

from .models import Pasta, Salad, DinnerPlate, Sub, SubExtra, Pizza

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlate)
admin.site.register(Sub)
admin.site.register(SubExtra)