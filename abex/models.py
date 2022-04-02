from django.contrib.auth.models import AbstractUser
from django.db import models
from django_clickhouse.models import ClickHouseSyncModel

STATUS_OF_TRANSACTION = (
    ('accrual', 'Accrual'),
    ('write-off', 'Write-off')
)

class TypeOfService(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    point = models.IntegerField(default=0, blank=False, null=False)


class User(AbstractUser):
    last_active = models.DateTimeField(auto_now=True)
    point = models.PositiveIntegerField(default=0)


class Transaction(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Author')
    created_at = models.DateTimeField(auto_now=True)
    type_of_service = models.ForeignKey(TypeOfService, on_delete=models.CASCADE, related_name='Type',default=0)
    status = models.CharField(choices=STATUS_OF_TRANSACTION, default='Accrual', max_length=15)
