from datetime import datetime
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from clients.models import ClientModel

from message_sender.tasks import message_task

class MessageSenderModel(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    message = models.TextField()
    client_tag = models.CharField(max_length=20)

    def __str__(self):
        return f'Сообщение: {self.message} Тег: {self.client_tag}'


class MessageModel(models.Model):
    class Meta:
        ordering = ['-status']
    
    datetime_stamp = models.DateTimeField()
    status = models.BooleanField(default=False)
    message_sender_id = models.ForeignKey(MessageSenderModel, null=False, blank=False, on_delete=models.CASCADE)
    client_id = models.ForeignKey(ClientModel, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.client_id} {self.datetime_stamp} {self.status}'

@receiver(post_save, sender=MessageSenderModel)
def messaging(sender, instance, created, **kwargs):
    if created:
        time = instance.start_datetime
        #TODO: Необходима правильная настройка таймзон
        if time.replace(tzinfo=None) < timezone.now().replace(tzinfo=None):
            message_task.delay(instance.id, instance.end_datetime)
        else:
            message_task.apply_async(args=[instance.id, instance.end_datetime], eta=time)