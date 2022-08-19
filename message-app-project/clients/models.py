import pytz

from django.db import models
from django.core.validators import RegexValidator


TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

class ClientModel(models.Model):
    phone = models.CharField(
        max_length=11,
        help_text='Формат: 7XXXXXXXXXX',
        validators=[RegexValidator(
            r'^[7]{1}?[0-9]{10}',
            message='Введите корректный номер')]
        )
    mobile_operator_code = models.CharField(
        max_length=9,
        help_text='Код мобильного оператора',
        validators=[RegexValidator(
            r'^[0-9]*$',
            message='Введите корректный код')]
        )

    tag = models.CharField(max_length=20)

    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='Europe/Moscow')

    def __str__(self):
        return f'{self.phone} - {self.tag}'
        