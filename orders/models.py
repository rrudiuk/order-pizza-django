from django.db import models
from decimal import Decimal

# Create your models here.
SIZE = [
	('L', 'L'),
	('S', 'S'),
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
	size = models.CharField(max_length=1, choices=SIZE)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"Your Dinner Plate: {self.name}, size {self.size}, price {self.price}"

class SubExtra(models.Model):
	name = models.CharField(max_length = 64)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name}"

class Sub(models.Model):
	name = models.CharField(max_length = 64)
	size = models.CharField(max_length=1, choices=SIZE)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	extra = models.ManyToManyField(SubExtra, blank=True, related_name="extra")

	def __str__(self):
		if self.extra.count() == 0:
			return f"Your Sub: {self.name}, size {self.size}, price {self.price}"
		else:
			price = Decimal(self.price) + Decimal(0.50)
			return f"Your Sub: {self.name}, size {self.size}, {self.extra.get()}, price {price}"