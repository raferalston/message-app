from time import sleep

from celery import shared_task
from celery.utils.log import get_task_logger

from message_sender.message_handler import start_messaging


logger = get_task_logger(__name__)

@shared_task
def message_task(instance, end_time):
    logger.info("message_task just ran")
    start_messaging(instance, end_time.split('+')[0])