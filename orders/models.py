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

	def __str__(self):
		return f"You Pasta: {self.name}, price {self.price}"

# Model for Salad
class Salad(models.Model):
	name = models.CharField(max_length = 64)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"Your Salad: {self.name}, price {self.price}"

# Model for Dinner Plate
class DinnerPlate(models.Model):
	name = models.CharField(max_length = 64)
	size = models.CharField(max_length=5, choices=SIZE)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"Your Dinner Plate: {self.name}, size: {self.size}, price {self.price}"

class SubExtra(models.Model):
	name = models.CharField(max_length = 64)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name}"

class Sub(models.Model):
	name = models.CharField(max_length = 64)
	size = models.CharField(max_length=5, choices=SIZE)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	extra = models.ManyToManyField(SubExtra, blank=True, related_name="extra")

	def __str__(self):
		if self.extra.count() == 0:
			return f"Your Sub: {self.name}, size: {self.size}, price {self.price}"
		else:
			price = Decimal(self.price) + Decimal(0.50)
			return f"Your Sub: {self.name}, size: {self.size}, {self.extra.get()}, price {price}"
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

	def __str__(self):
		return f"{self.name}"

class Pizza(models.Model):
	name = models.CharField(max_length=64, choices=PIZZA)
	size = models.CharField(max_length=5, choices=SIZE)
	topping = models.CharField(max_length=32, choices=TOPPINGS)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"Your Pizza: {self.name}, size: {self.size}, topping: {self.topping}, price {self.price}"