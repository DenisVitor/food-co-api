from uuid import uuid4
from django.db import models


# Create your models here.
class FlavorChoices(models.TextChoices):
    SAVORY = "Savory"
    SWEET = "Sweet"


class PrepareChoices(models.TextChoices):
    FRIED = "Fried"
    COOKED = "Cooked"
    FREEZED = "Freezed"
    GRILLED = "Grilled"
    NATURAL = "Natural"
    BAKED = "Baked"


class SizeChoices(models.TextChoices):
    SMALL = "Small"
    REGULAR = "Regular"
    LARGE = "Large"


class Snack(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200, unique=True)
    image = models.TextField()
    flavor = models.CharField(
        max_length=100, choices=FlavorChoices.choices, default=FlavorChoices.SAVORY
    )
    prepare = models.CharField(
        max_length=100, choices=PrepareChoices.choices, default=PrepareChoices.FRIED
    )
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    size = models.CharField(
        max_length=100, choices=SizeChoices.choices, default=SizeChoices.REGULAR
    )
    quantity = models.IntegerField(default=1)
