from datetime import datetime

from rest_framework import status

from django.urls import reverse
from django.test import TestCase, Client

from clients.models import ClientModel
from .models import MessageSenderModel, MessageModel


c = Client()

class MessageStatisticsTestCase(TestCase):
    """Because this viewset is read-only, i decide to dont make routine tests for it."""
    pass

class MessageSenderModelDrfTestCase(TestCase):
    def setUp(self):
        self.start_date = datetime.now()
        self.end_date = datetime.now()

    def test_post_bank(self):
        url = reverse('messages-list')
        data = {
            'start_datetime': self.start_date,
            'end_datetime': self.end_date,
            'message': 'test drf',
            'client_tag': 'test tag'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MessageSenderModel.objects.count(), 1)
        self.assertEqual(MessageSenderModel.objects.get().message, 'test drf')

    def test_patch_bank(self):
        url = reverse('messages-list')
        data = {
            'start_datetime': self.start_date,
            'end_datetime': self.end_date,
            'message': 'test drf',
            'client_tag': 'test tag'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MessageSenderModel.objects.count(), 1)
        self.assertEqual(MessageSenderModel.objects.get().message, 'test drf')

        url = reverse('messages-detail', args=(1,))
        import json 
        data = json.dumps({'message': 'test drf change'})
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(MessageSenderModel.objects.get().message, 'test drf change')

    def test_delete_bank(self):
        url = reverse('messages-detail', args=(1,))
        response = self.client.delete(url)
        self.assertEqual(MessageSenderModel.objects.count(), 0)

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
