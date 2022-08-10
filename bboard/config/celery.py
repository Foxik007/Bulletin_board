import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')
#app.conf.beat_schedule = {
#    'print_every_5_seconds': {
#        'task': 'blog.tasks.last_post',
#        'schedule': crontab(),
#    },
#}

app.autodiscover_tasks()