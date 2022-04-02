from django_clickhouse.models import ClickHouseSyncModel
from django.db import models


class UserClick(ClickHouseSyncModel):
    first_name = models.CharField(max_length=50)
    visits = models.IntegerField(default=0)
    birthday = models.DateField()


class PointCountClick(ClickHouseSyncModel):
    created_at = models.DateTimeField(auto_now=True)
    total_point = models.IntegerField()
