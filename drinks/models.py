from django.db import models
from uuid import uuid4


# Create your models here.
class FlavorChoices(models.TextChoices):
    COLA = "Cola"
    LEMON = "Lemon"
    GRAPE = "Grape"
    STRAWBERRY = "Strawberry"
    CHERRY = "Cherry"


class TypeChoices(models.TextChoices):
    SODA = "Soda"
    JUICE = "Juice"
    TEA = "Iced Tea"
    COFFEE = "Iced Coffee"
    SMOOTHIE = "Smoothie"


class SizeChoices(models.TextChoices):
    SMALL = "Small"
    REGULAR = "Regular"
    LARGE = "Large"


class Drink(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.TextField(blank=True)
    flavor = models.CharField(
        max_length=100, choices=FlavorChoices.choices, default=FlavorChoices.COLA
    )
    drink_type = models.CharField(
        max_length=100, choices=TypeChoices.choices, default=TypeChoices.SODA
    )
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    size = models.CharField(
        max_length=100, choices=SizeChoices.choices, default=SizeChoices.REGULAR
    )
