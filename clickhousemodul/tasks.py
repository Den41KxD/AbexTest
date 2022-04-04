from celery import shared_task
from django.db.models import Sum
from datetime import timedelta
from abex.models import User
from TestAbex.celery import app
from .clickhouse_models import ClickhousePoint


@shared_task()
def add():
    total_point = User.objects.all().aggregate(Sum('point'))
    print(total_point.get('point__sum'))
    ClickhousePoint.objects.create(total_point=total_point.get('point__sum'))
    if total_point.get('point__sum') > 10000:
        print('Warning: total_point : ' + str(total_point.get('point__sum')))


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'clickhousemodul.tasks.add',
        'schedule': timedelta(seconds=10)
    },
}
