from django.http import HttpResponse
from django.shortcuts import render

from .models import Pasta, DinnerPlate, Sub, SubExtra

# Create your views here.
def index(request):
    context = {
        "pasta": Pasta.objects.all(),
        "dinner_plate": DinnerPlate.objects.all(),
        "subs": Sub.objects.all(),
        "subextras": SubExtra.objects.all()
    }

    return render(request, "orders/index.html", context)
