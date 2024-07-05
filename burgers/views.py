from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from burgers.models import Burger
from burgers.serializers import BurgerSerializer

# Create your views here.


class BurguerView(ListCreateAPIView):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer


class BurgerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer
    lookup_url_kwarg = "burger_id"
