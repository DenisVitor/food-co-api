from rest_framework import serializers
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        extra_kwargs = {"order": {"read_only": True}}

    def create(self, validated_data) -> Client:
        return Client.objects.create(**validated_data)
