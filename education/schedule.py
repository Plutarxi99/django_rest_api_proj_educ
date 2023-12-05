# import json
# from datetime import datetime, timedelta
#
# from django_celery_beat.models import IntervalSchedule, PeriodicTask

#  ???????????????????????????
# def set_schedule(*args, **kwargs):
#     schedule, created = IntervalSchedule.objects.get_or_create(
#         every=10,
#         period=IntervalSchedule.SECONDS,
#     )
#     PeriodicTask.objects.create(
#         interval=schedule,  # we created this above.
#         name='Уведомление об изменние курса',  # simply describes this periodic task.
#         task='education.tasks.check_condition',  # name of task.
#         args=json.dumps(['arg1', 'arg2']),
#         kwargs=json.dumps({
#             'be_careful': True,
#         }),
#         expires=datetime.utcnow() + timedelta(seconds=30)
#     )