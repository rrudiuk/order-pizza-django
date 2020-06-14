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
	# size = models.CharField(max_length=5, choices=SIZE)
	priceS = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	priceL = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	hash_name = models.CharField(max_length = 64)

	def __str__(self):
		if self.priceS != 0.00 and self.priceL != 0.00:
			return f"{self.name}, small: {self.priceS}, large: {self.priceL}"
		elif self.priceS == 0.00:
			return f"{self.name}, large: {self.priceL}"
		else:
			return f"{self.name}, small: {self.priceS}"

class SubExtraAll(models.Model):
	name = models.CharField(max_length = 64)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	hash_name = models.CharField(max_length = 64)

	def __str__(self):
		return f"{self.name}"

class SubExtraSteak(models.Model):
	name = models.CharField(max_length = 64)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	hash_name = models.CharField(max_length = 64)

	def __str__(self):
		return f"{self.name}"

class Sub(models.Model):
	name = models.CharField(max_length = 64)
	# size = models.CharField(max_length=5, choices=SIZE)
	priceS = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	priceL = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	hash_name = models.CharField(max_length = 64)
	extra = models.ManyToManyField(SubExtraAll, blank=True, related_name="extra")
	extraSteak = models.ManyToManyField(SubExtraSteak, blank=True, related_name="extra_steak")

	def __str__(self):
		if self.priceS != 0.00 and self.priceL != 0.00:
			return f"{self.name}, small: {self.priceS}, large: {self.priceL}"
		elif self.priceS == 0.00:
			return f"{self.name}, large: {self.priceL}"
		else:
			return f"{self.name}, small: {self.priceS}"

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
	extra = models.CharField(max_length = 64, blank=True, default = "empty")
	extra_steak = models.CharField(max_length = 64, blank=True, default = "empty")
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		# Pasta and Salad
		if not self.size:
			return f"{self.name}, {self.price}"
		# Subs without extra
		elif self.extra == "empty" and self.extra_steak == "empty":
			return f"{self.name}, {self.size}, {self.price}"
		# Subs with extra cheese
		elif self.extra != "empty" and self.extra_steak == "empty":
			price = Decimal(self.price) + Decimal(0.50)
			return f"{self.name}, {self.size}, with {self.extra}, {price}"
		# Sub Steak + Cheese with extra
		elif self.extra == "empty" and self.extra_steak != "empty":
			price = Decimal(self.price) + Decimal(0.50)
			return f"{self.name}, {self.size}, with {self.extra_steak}, {price}"
		# Sub Steak + Cheese with extra and extra cheese
		elif self.extra != "empty" and self.extra_steak != "empty":
			price = Decimal(self.price) + Decimal(1.00)
			return f"{self.name}, {self.size}, with {self.extra} and {self.extra_steak}, {price}"
		else:
			return f"{self.name}, {self.size}, {self.price}"
