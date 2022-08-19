from time import sleep

from celery import shared_task

from message_sender.message_handler import start_messaging

@shared_task
def message_task(instance, end_time):
    print(end_time.split('+')[0])
    start_messaging(instance, end_time.split('+')[0])