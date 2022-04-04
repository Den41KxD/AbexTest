from __future__ import absolute_import
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestAbex.settings')

from django.conf import settings  # noqa

broker_url = 'redis://localhost'
app = Celery('clickhousemodul.tasks', broker=broker_url, backend=broker_url)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.timezone = 'UTC'