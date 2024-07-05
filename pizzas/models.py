from uuid import uuid4
from django.db import models


class ChesseChoices(models.TextChoices):
    MOZZARELA = "Mozzarela"
    PROVOLONE = "Provolone"
    CHEDDAR = "Cheddar"
    PARMESAN = "Parmesan"
    ASIAGO = "Asiago"


class MeatChoices(models.TextChoices):
    PEPPERONI = ("Pepperoni",)
    GROUND_MEAT = "Ground Meat"
    ITALIAN_SAUSAGE = "Italian Sausage"
    CHICKEN = ("Chicken",)
    HAM = "Ham"


class SizeChoices(models.TextChoices):
    SMALL = "Small"
    REGULAR = "Regular"
    LARGE = "Large"


# Create your models here.
class Pizza(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200, blank=True)
    image = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    description = models.TextField(blank=True)
    meat_one = models.CharField(
        max_length=100,
        choices=MeatChoices.choices,
        null=False,
        default=MeatChoices.PEPPERONI,
    )
    meat_two = models.CharField(
        max_length=100, choices=MeatChoices.choices, null=True, default=None
    )
    meat_three = models.CharField(
        max_length=100, choices=MeatChoices.choices, null=True, default=None
    )
    cheese_one = models.CharField(
        max_length=100, choices=ChesseChoices.choices, default=ChesseChoices.MOZZARELA
    )
    cheese_two = models.CharField(
        max_length=100, choices=ChesseChoices.choices, null=True, default=None
    )
    cheese_three = models.CharField(
        max_length=100, choices=ChesseChoices.choices, null=True, default=None
    )
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    size = models.CharField(
        max_length=100, choices=SizeChoices.choices, default=SizeChoices.REGULAR
    )
