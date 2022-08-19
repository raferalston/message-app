from datetime import datetime

from django.test import TestCase

from clients.models import ClientModel
from .models import MessageSenderModel, MessageModel

class MessageModelTestCase(TestCase):
    def setUp(self):
        self.start_date = datetime.now()
        self.end_date = datetime.now()
        self.message_sender_model = MessageSenderModel.objects.create(
            start_datetime=self.start_date, 
            end_datetime=self.end_date,
            message='test',
            client_tag='test'
            )
        self.client_model = ClientModel.objects.create(
            phone='79999999999', 
            mobile_operator_code='999',
            tag='test'
            )
        MessageModel.objects.create(
            datetime_stamp=self.start_date,
            status=True,
            message_sender_id=self.message_sender_model,
            client_id=self.client_model
        )

    def test_proper_client_creation(self):
        message_model = MessageModel.objects.get(datetime_stamp=self.start_date)
        self.assertEqual(message_model.status, True)
        


class MessageSenderModelTestCase(TestCase):
    def setUp(self):
        self.start_date = datetime.now()
        self.end_date = datetime.now()
        MessageSenderModel.objects.create(
            start_datetime=self.start_date, 
            end_datetime=self.end_date,
            message='test',
            client_tag='test'
            )

    def test_proper_client_creation(self):
        message_model = MessageSenderModel.objects.get(start_datetime=self.start_date)
        self.assertEqual(message_model.message, 'test')
