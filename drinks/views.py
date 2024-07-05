from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drinks.models import Drink
from drinks.serializers import DrinkSerializer

# Create your views here.


class DrinkView(ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class DrinkDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    lookup_url_kwarg = "drink_id"
