from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from clients.models import Client
from clients.serializers import ClientSerializer

# Create your views here.


class ClientView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_url_kwarg = "client_id"
