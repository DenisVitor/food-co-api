from rest_framework.generics import ListCreateAPIView
from models import Account
from serializers import AccountSerializer

# Create your views here.


class AccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
