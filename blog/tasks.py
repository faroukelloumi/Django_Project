from __future__ import absolute_import

from celery import shared_task
from celery import current_task, Task
from celery.utils.log import get_task_logger
from core.celery import app
import logging

logger = logging.getLogger()


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@app.task()
def test_task():
    logger.warning("celerrrrrrrrrry log")
    print "test"
    return True