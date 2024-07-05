from django.db import models
from uuid import uuid4
from clients.models import Client

# Create your models here.


class Order(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    description = models.CharField(null=True, max_length=200, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True)
    delivering_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    ordered_since = models.DateTimeField(auto_now_add=True)
    order_updated = models.DateTimeField(auto_now=True)
    burger = models.ManyToManyField("burgers.Burger", related_name="orders")
    snack = models.ManyToManyField("snacks.Snack", related_name="orders")
    drink = models.ManyToManyField("drinks.Drink", related_name="orders")
    pizza = models.ManyToManyField("pizzas.Pizza", related_name="orders")

    def formatted_date(self):
        return self.created_at.strftime("%B %d, %Y at %I:%M %p")
