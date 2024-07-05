from rest_framework import serializers
from drinks.models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = "__all__"
        extra_kwargs = {"order": {"read_only": True}}

    def create(self, validated_data) -> Drink:
        return Drink.objects.create(**validated_data)
