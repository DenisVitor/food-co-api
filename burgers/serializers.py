from rest_framework import serializers
from burgers.models import Burger


class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = "__all__"
        extra_kwargs = {"order": {"read_only": True}}

    def create(self, validated_data) -> Burger:
        return Burger.objects.create(**validated_data)
