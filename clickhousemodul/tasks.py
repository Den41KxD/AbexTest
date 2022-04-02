from celery import Celery

broker_url = 'redis://127.0.0.1:6379'
app = Celery('tasks', broker=broker_url, backend=broker_url)


from celery import shared_task


@shared_task
def add():
    print('hello')
