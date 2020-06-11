from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Pasta, DinnerPlate, Sub, SubExtraAll, SubExtraSteak, Salad, Pizza, Topping, Order

# Create your views here.
def index(request):

    username = ""

    if request.user.is_authenticated:
        username = request.user

        if request.method == 'POST' and request.POST["select-food-type"] != 'empty':

            food_type = request.POST["select-food-type"]

            if food_type == 'salad':
                food_name = request.POST["salad-name"]
                db_query = Salad.objects.get(hash_name = food_name)
                order = Order(name = db_query.name, price = db_query.price)
                order.save()
                username = db_query.name

            elif food_type == 'pasta':
                food_name = request.POST["pasta-name"]
                db_query = Pasta.objects.get(hash_name = food_name)
                order = Order(name = db_query.name, price = db_query.price)
                order.save()
                username = db_query.name

            else:
                username = food_type


    context = {
            "pasta": Pasta.objects.all(),
            "salads": Salad.objects.all(),
            "dinner_plate": DinnerPlate.objects.all(),
            "subs": Sub.objects.all(),
            "subextraall": SubExtraAll.objects.all(),
            "subextrasteak": SubExtraSteak.objects.all(),
            "pizzas": Pizza.objects.all(),
            "toppings": Topping.objects.all(),
            "orders": Order.objects.all(),
            "user": username,
        }

    return render(request, "orders/index.html", context)

def login_view(request):
    return render(request, "orders/login.html")
