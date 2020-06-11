from django.db import models
from decimal import Decimal

# Create your models here.
SIZE = [
	('Large', 'Large'),
	('Small', 'Small'),
]
# Model for Pasta
class Pasta(models.Model):
	name = models.CharField(max_length = 64)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	hash_name = models.CharField(max_length = 64)

	def __str__(self):
		return f"Pasta {self.name}, price {self.price}"

# Model for Salad
class Salad(models.Model):
	name = models.CharField(max_length = 64)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	hash_name = models.CharField(max_length = 64)

	def __str__(self):
		return f"Salad {self.name}, price {self.price}"

# Model for Dinner Plate
class DinnerPlate(models.Model):
	name = models.CharField(max_length = 64)
	size = models.CharField(max_length=5, choices=SIZE)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	food_type = "Dinner Plate"

	def __str__(self):
		return f"Your Dinner Plate: {self.name}, size: {self.size}, price {self.price}"

class SubExtraAll(models.Model):
	name = models.CharField(max_length = 64)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	food_type = "Sub Extra"

	def __str__(self):
		return f"{self.name}"

class SubExtraSteak(models.Model):
	name = models.CharField(max_length = 64)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	food_type = "Sub Extra Steak Cheese"

	def __str__(self):
		return f"{self.name}"

class Sub(models.Model):
	name = models.CharField(max_length = 64)
	size = models.CharField(max_length=5, choices=SIZE)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	extra = models.ManyToManyField(SubExtraAll, blank=True, related_name="extra")
	extraSteak = models.ManyToManyField(SubExtraSteak, blank=True, related_name="extra_steak")
	food_type = "Subs"

	def __str__(self):
		return f"Your Sub: {self.name}, size: {self.size}, price {self.price}"

	# def __str__(self):
	# 	if self.extra.count() == 0:
	# 		return f"Your Sub: {self.name}, size: {self.size}, price {self.price}"
	# 	else:
	# 		price = Decimal(self.price) + Decimal(0.50)
	# 		return f"Your Sub: {self.name}, size: {self.size}, {self.extra.get()}, price {price}"

PIZZA = [
	('Regular', 'Regular'),
	('Sicilian', 'Sicilian')
]

TOPPINGS = 	[
	('Cheese', 'Cheese'),
	('1', '1 topping'),
	('2', '2 toppings'),
	('3', '3 toppings'),
	('Special', 'Special')
]

class Topping(models.Model):
	name = models.CharField(max_length = 64)
	food_type = "Toppings"

	def __str__(self):
		return f"{self.name}"

class Pizza(models.Model):
	name = models.CharField(max_length=64, choices=PIZZA)
	size = models.CharField(max_length=5, choices=SIZE)
	topping = models.CharField(max_length=32, choices=TOPPINGS)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	food_type = "Pizza"

	def __str__(self):
		return f"Your Pizza: {self.name}, size: {self.size}, topping: {self.topping}, price {self.price}"

class Order(models.Model):
	name = models.CharField(max_length = 64)
	size = models.CharField(max_length=5, blank=True)
	exta = models.CharField(max_length = 64, blank=True)
	extra_steak = models.CharField(max_length = 64, blank=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		if not self.size:
			return f"{self.name}, {self.price}"
		else:
			price = Decimal(self.price) + Decimal(0.50)
			return f"{self.name}, {self.size}, {price}"
