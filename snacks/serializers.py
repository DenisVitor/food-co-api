from rest_framework import serializers
from snacks.models import Snack


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = "__all__"

    def create(self, validated_data):
        return Snack.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.flavor = validated_data.get("flavor", instance.flavor)
        instance.prepare = validated_data.get("prepare", instance.prepare)
        instance.price = validated_data.get("price", instance.price)
        instance.description = validated_data.get(
            "description", instance.description)
        instance.rating = validated_data.get("rating", instance.rating)
        instance.size = validated_data.get("size", instance.size)

        return super().update(instance, validated_data)
