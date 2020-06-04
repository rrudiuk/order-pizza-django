from django.contrib import admin

from .models import Pasta, Salad, DinnerPlate, Sub, SubExtra

# Register your models here.
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlate)
admin.site.register(Sub)
admin.site.register(SubExtra)