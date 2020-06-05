from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Pasta, DinnerPlate, Sub, SubExtra, Salad, Pizza, Topping

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        context = {
            "pasta": Pasta.objects.all(),
            "salads": Salad.objects.all(),
            "dinner_plate": DinnerPlate.objects.all(),
            "subs": Sub.objects.all(),
            "subextras": SubExtra.objects.all(),
            "pizzas": Pizza.objects.all(),
            "toppings": Topping.objects.all(),
            "user": "",
        }

        return render(request, "orders/index.html", context)

    context = {
            "pasta": Pasta.objects.all(),
            "salads": Salad.objects.all(),
            "dinner_plate": DinnerPlate.objects.all(),
            "subs": Sub.objects.all(),
            "subextras": SubExtra.objects.all(),
            "pizzas": Pizza.objects.all(),
            "toppings": Topping.objects.all(),
            "user": request.user,
        }

    return render(request, "orders/index.html", context)

def login_view(request):
    return render(request, "orders/login.html")
