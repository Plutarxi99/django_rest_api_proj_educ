
import os

from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'education.tasks.check_condition',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
#     'check_user_last_login': {
#         'task': 'users.tasks.check_last_login',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }