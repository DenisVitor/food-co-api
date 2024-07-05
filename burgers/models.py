from django.db import models
from uuid import uuid4


# Create your models here.
class PattyChoices(models.TextChoices):
    BURGER = "Burger"
    CHICKEN = "Chicken"
    FISH = "Fish"
    GROUND_BEEF = "Ground Beef"
    RIBS = "Ground Ribs"


class CheeseChoices(models.TextChoices):
    AMERICAN = "American Cheese"
    CHEDDAR = "Cheddar"
    PEPPER = "Pepper Jack"
    MONTEREY = "Monterey Jack"
    PROVOLONE = "Provolone"


class SizeChoices(models.TextChoices):
    SMALL = "Small"
    REGULAR = "Regular"
    LARGE = "Large"


class Burger(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    patty_one = models.CharField(
        max_length=100, choices=PattyChoices.choices, default=PattyChoices.BURGER
    )
    patty_two = models.CharField(
        max_length=100, choices=PattyChoices.choices, null=True, default=None
    )
    patty_three = models.CharField(
        max_length=100, choices=PattyChoices.choices, null=True, default=None
    )
    cheese_one = models.CharField(
        max_length=100, choices=CheeseChoices.choices, default=CheeseChoices.AMERICAN
    )
    cheese_two = models.CharField(
        max_length=100, choices=CheeseChoices.choices, null=True, default=None
    )
    cheese_three = models.CharField(
        max_length=100, choices=CheeseChoices.choices, null=True, default=None
    )
    size = models.CharField(
        max_length=100, choices=SizeChoices.choices, default=SizeChoices.REGULAR
    )
