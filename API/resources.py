from rest_framework.viewsets import ModelViewSet
from abex.models import User, Transaction, TypeOfService
from API.serializers import UserSerializers, TransactionSerializers, TypeOfServiceSerializers


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializers
    queryset = Transaction.objects.all()


class SeriviceViewSet(ModelViewSet):
    serializer_class = TypeOfServiceSerializers
    queryset = TypeOfService.objects.all()


class PointZeroView(ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.filter(point=0)


class PointNonZeroView(ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.filter(point__gt=1000)

