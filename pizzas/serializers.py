from rest_framework import serializers
from pizzas.models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"
        extra_kwargs = {"order": {"read_only": True}}

    def create(self, validated_data) -> Pizza:
        return Pizza.objects.create(**validated_data)
