#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# by Qige <qigezhao@gmail.com> since 2020-08-09

from datetime import timedelta
from celery.schedules import crontab

# celery basic settings
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_TASK_RESULT_EXPIRES = 60 * 15
CELERY_EVENT_QUEUE_TTL = 5

CELERYD_TASK_TIME_LIMIT = 60 * 15
CELERYD_MAX_TASK_PER_CHILD = 20
CELERYD_FORCE_EVECV = True

# payload pack/unpack between celery worker
CELERY_ACCEPT_CONTENT = [
    'msgpack'
]
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_MESSAGE_COMPRESSION = 'zlib'

# celery components
CELERY_IMPORTS = (
    'celery_app.task_probe',
    'celery_app.beat_weather',
)

# scheduled celery tasks with params
CELERYBEAT_SCHEDULE = {
    'beat_sync_city_weather': {
        'task': 'celery_app.beat_weather.beat_fetch_weather',
        'schedule': crontab(hour='*/1'),
        # 'schedule': timedelta(seconds=5),
        'args': (),
    }
}
