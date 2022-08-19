from django.db import models

from clients.models import ClientModel


class MessageSenderModel(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    message = models.TextField()
    client_tag = models.CharField(max_length=20)

    def __str__(self):
        return f'Сообщение: {self.message} Тег: {self.client_tag}'

class MessageModel(models.Model):
    datetime_stamp = models.DateTimeField()
    status = models.BooleanField(default=False)
    message_sender_id = models.ForeignKey(MessageSenderModel, null=False, blank=False, on_delete=models.CASCADE)
    client_id = models.ForeignKey(ClientModel, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.datetime_stamp} {self.status}'