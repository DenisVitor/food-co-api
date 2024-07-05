from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from snacks.models import Snack
from snacks.serializers import SnackSerializer
from bson import decimal128
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class SnackView(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    lookup_url_kwarg = "snack_id"

    def patch(self, request, *args, **kwargs):
        snack_id = kwargs.get("snack_id")
        snack = get_object_or_404(Snack, id=snack_id)

        data = request.data

        if "price" in data:
            try:
                data["price"] = decimal128.Decimal128(str(data["price"]))
            except (TypeError, ValueError, decimal128.InvalidOperation):
                return Response(
                    {"error": "Price must be a valid Decimal128 number."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        serializer = SnackSerializer(snack, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
