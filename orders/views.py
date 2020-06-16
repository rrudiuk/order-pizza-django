from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum

from .models import Pasta, DinnerPlate, Sub, SubExtraAll, SubExtraSteak, Salad, Pizza, Topping, Order

# Create your views here.
def index(request):

    username = ""
    user_id = ""
    message = ""

    if request.user.is_authenticated:
        username = request.user
        user_id = request.user.id

        db_order_sum = Order.objects.filter(user_id = user_id).aggregate(total_price=Sum('price'))
        if db_order_sum["total_price"] is not None:
            order_price = round(db_order_sum["total_price"], 2)
        else:
            order_price = 0

        if request.method == 'POST' and request.POST["select-food-type"] != 'empty':

            food_type = request.POST["select-food-type"]

            # If Salad was selected
            if food_type == 'salad':
                food_name = request.POST["salad-name"]
                db_query = Salad.objects.get(hash_name = food_name)
                order = Order(user_id = request.user.id, name = db_query.name, price = db_query.price)
                order.save()

            # If Pasta was selected
            elif food_type == 'pasta':
                food_name = request.POST["pasta-name"]
                db_query = Pasta.objects.get(hash_name = food_name)
                order = Order(user_id = request.user.id, name = db_query.name, price = db_query.price)
                order.save()

            # If Sub was selected
            elif food_type == 'sub':
                food_name = request.POST["sub-name"]
                food_size = request.POST["size"]
                if food_name != "empty" and food_size != "empty":
                    db_query = Sub.objects.get(hash_name = food_name)
                    if food_size == 'small':
                        order = Order(user_id = request.user.id, name = db_query.name, size = food_size, price = db_query.priceS)
                    else:
                        order = Order(user_id = request.user.id, name = db_query.name, size = food_size, price = db_query.priceL)
                    order.save()
                    # Add extra if selected
                    food_extra = request.POST["extra-all"]
                    if food_extra != 'empty':
                        extra = SubExtraAll.objects.get(hash_name = food_extra)
                        order.extra = extra.name
                    steak_extra = request.POST["extra-steak"]
                    # Add steak extra if selected
                    if steak_extra != 'empty':
                        extra_steak = SubExtraSteak.objects.get(hash_name = steak_extra)
                        order.extra_steak = extra_steak.name
                    order.save()
                else:
                    message = "Please select all the necessary items."


            # If Dinner Plate was selected
            elif food_type == 'dinner_plate':
                food_name = request.POST["dinner-plate"]
                food_size = request.POST["size"]
                if food_name != "empty" and food_size != "empty":
                    db_query = DinnerPlate.objects.get(hash_name = food_name)
                    if food_size == 'small':
                        order = Order(user_id = request.user.id, name = db_query.name, size = food_size, price = db_query.priceS)
                    else:
                        order = Order(user_id = request.user.id, name = db_query.name, size = food_size, price = db_query.priceL)
                    order.save()
                else:
                    message = "Please select all the necessary items."

            # If Pizza was selected
            elif food_type == 'pizza':
                food_name = request.POST["pizza-type"]
                food_size = request.POST["size"]
                toppings = request.POST["topping-number"]
                db_query = Pizza.objects.get(hash_name = food_name)
                if food_size == 'small':
                    order = Order(user_id = request.user.id, name = db_query.name + ' pizza, ' + toppings, size = food_size, 
                        price = db_query.cheeseS)
                else:
                    order = Order(user_id = request.user.id, name = db_query.name + ' pizza, ' + toppings, size = food_size, 
                        price = db_query.cheeseL)
                order.save()

                # Pizza with 1 topping
                if toppings == '1 topping':
                    # Add topping
                    topping1_name = request.POST["topping1"]
                    db_topping1_query = Topping.objects.get(hash_name = topping1_name)
                    order.topping1 = db_topping1_query.name
                    # Set the price
                    if food_size == 'small':
                        order.price = db_query.toppin1S
                    else:
                        order.price = db_query.toppin1L

                # Pizza with 2 toppings
                if toppings == '2 toppings':
                    # Add first topping
                    topping1_name = request.POST["topping1"]
                    db_topping1_query = Topping.objects.get(hash_name = topping1_name)
                    order.topping1 = db_topping1_query.name
                    # Add second topping
                    topping2_name = request.POST["topping2"]
                    db_topping2_query = Topping.objects.get(hash_name = topping2_name)
                    order.topping2 = db_topping2_query.name
                    # Set the price
                    if food_size == 'small':
                        order.price = db_query.toppin2S
                    else:
                        order.price = db_query.toppin2L

                # Pizza with 3 toppings
                if toppings == '3 toppings':
                    # Add first topping
                    topping1_name = request.POST["topping1"]
                    db_topping1_query = Topping.objects.get(hash_name = topping1_name)
                    order.topping1 = db_topping1_query.name
                    # Add second topping
                    topping2_name = request.POST["topping2"]
                    db_topping2_query = Topping.objects.get(hash_name = topping2_name)
                    order.topping2 = db_topping2_query.name
                    # Add third topping
                    topping3_name = request.POST["topping3"]
                    db_topping3_query = Topping.objects.get(hash_name = topping3_name)
                    order.topping3 = db_topping3_query.name
                    # Set the price
                    if food_size == 'small':
                        order.price = db_query.toppin3S
                    else:
                        order.price = db_query.toppin3L

                # Special pizza
                if toppings == 'special':
                    # Set the price
                    if food_size == 'small':
                        order.price = db_query.specialS
                    else:
                        order.price = db_query.specialL
                order.save()



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
            "user_id": user_id,
            "order_price": order_price,
            "message": message,
        }

    return render(request, "orders/index.html", context)

def login_view(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def cart(request):
    if request.user.is_authenticated:

        user_id = request.user.id

        if request.method == 'POST':
            Order.objects.filter(user_id = user_id).delete()

        db_order_sum = Order.objects.filter(user_id = user_id).aggregate(total_price=Sum('price'))
        if db_order_sum["total_price"] is not None:
            order_price = round(db_order_sum["total_price"], 2)
        else:
            order_price = 0

        context = {
            "orders": Order.objects.all(),
            "user_id": user_id,
            "order_price": order_price,
            "message": "This is your order:"
        }

        return render(request, "orders/cart.html", context)

    else:
        return render(request, "orders/cart.html", {"message": "Please log in to access cart."})