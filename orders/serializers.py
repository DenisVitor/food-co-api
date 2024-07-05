from rest_framework import serializers
from django.forms.models import model_to_dict
from orders.models import Order
from clients.models import Client
from burgers.models import Burger
from snacks.models import Snack
from drinks.models import Drink
from pizzas.models import Pizza


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.UUIDField(required=True)
    burger = serializers.ListSerializer(child=serializers.UUIDField(), required=False)
    snack = serializers.ListSerializer(child=serializers.UUIDField(), required=True)
    drink = serializers.ListSerializer(child=serializers.UUIDField(), required=False)
    pizza = serializers.ListSerializer(child=serializers.UUIDField(), required=False)

    class Meta:
        model = Order
        fields = [
            "id",
            "description",
            "client",
            "delivering_price",
            "total_price",
            "ordered_since",
            "order_updated",
            "burger",
            "snack",
            "drink",
            "pizza",
        ]

    def create(self, validated_data):
        burger_ids = validated_data.pop("burger", [])
        snack_ids = validated_data.pop("snack", [])
        drink_ids = validated_data.pop("drink", [])
        pizza_ids = validated_data.pop("pizza", [])
        client_id = validated_data.pop("client")

        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            raise serializers.ValidationError(
                f"Client with id {client_id} does not exist."
            )

        order = Order.objects.create(client=client, **validated_data)

        if burger_ids:
            burgers = Burger.objects.filter(id__in=burger_ids)
            order.burger.set(burgers)

        if snack_ids:
            snacks = Snack.objects.filter(id__in=snack_ids)
            order.snack.set(snacks)

        if drink_ids:
            drinks = Drink.objects.filter(id__in=drink_ids)
            order.drink.set(drinks)

        if pizza_ids:
            pizzas = Pizza.objects.filter(id__in=pizza_ids)
            order.pizza.set(pizzas)

        return order

