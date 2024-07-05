from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pizzas.models import Pizza
from pizzas.serializers import PizzaSerializer

# Create your views here.


class PizzaView(ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    lookup_url_kwarg = "pizza_id"
