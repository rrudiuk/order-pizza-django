from django.db import models
from decimal import Decimal

# Create your models here.
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

class Topping(models.Model):
	name = models.CharField(max_length = 64)
	hash_name = models.CharField(max_length = 64)

	def __str__(self):
		return f"{self.name}"

class Pizza(models.Model):
	name = models.CharField(max_length = 64)
	hash_name = models.CharField(max_length = 64)
	cheeseS = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	cheeseL = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	toppin1S = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	toppin1L = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	toppin2S = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	toppin2L = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	toppin3S = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	toppin3L = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	specialS = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	specialL = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)

	def __str__(self):
		return f"{self.name} pizza"

class Order(models.Model):
	user_id= models.IntegerField()
	name = models.CharField(max_length = 64)
	size = models.CharField(max_length=5, blank=True)
	extra = models.CharField(max_length = 64, default = "empty")
	extra_steak = models.CharField(max_length = 64, default = "empty")
	topping1 = models.CharField(max_length = 64, default = "empty")
	topping2 = models.CharField(max_length = 64, default = "empty")
	topping3 = models.CharField(max_length = 64, default = "empty")
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		# Pasta and Salad
		if not self.size:
			return f"{self.name}, {self.price}"
		elif self.topping3 != "empty":
			return f"{self.name}, {self.size}, with {self.topping1}, {self.topping2}, {self.topping3}, price: {self.price}"
		elif self.topping2 != "empty":
			return f"{self.name}, {self.size}, with {self.topping1}, {self.topping2}, price: {self.price}"
		elif self.topping1 != "empty":
			return f"{self.name}, {self.size}, with {self.topping1}, price: {self.price}"
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
