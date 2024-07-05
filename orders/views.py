from decimal import Decimal
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework.response import Response


# Create your views here.


class OrderReadView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        for order in data:
            order_id = order["id"]
            order_instance = Order.objects.get(id=order_id)
            order["client"] = {
                "name": order_instance.client.name,
                "email": order_instance.client.email,
                "address": order_instance.client.address,
                "phone": order_instance.client.phone,
                "avatar": order_instance.client.avatar,
            }
            order["burger"] = list(order_instance.burger.values())
            order["snack"] = list(order_instance.snack.values())
            order["drink"] = list(order_instance.drink.values())
            order["pizza"] = list(order_instance.pizza.values())

            for item in data:
                for key, value in item.items():
                    if isinstance(value, dict):
                        for sub_key, sub_value in value.items():
                            value[sub_key] = str(sub_value)
                    else:
                        item[key] = str(value)

        return Response(data)


class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderRetrieveView(RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_url_kwarg = "order_id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        data["client"] = {
            "name": instance.client.name,
            "email": instance.client.email,
            "address": instance.client.address,
            "phone": instance.client.phone,
            "avatar": instance.client.avatar,
        }
        data["burger"] = list(instance.burger.values())
        data["snack"] = list(instance.snack.values())
        data["drink"] = list(instance.drink.values())
        data["pizza"] = list(instance.pizza.values())

        for key, value in data.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    value[sub_key] = str(sub_value)
            else:
                data[key] = str(value)

        return Response(data)


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = "order_id"


class OrderDestroyView(DestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_url_kwarg = "order_id"
