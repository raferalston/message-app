from django.urls import reverse
from django.test import TestCase, Client

from rest_framework import status

from .models import ClientModel

c = Client()

class ClientModelTestCase(TestCase):
    def setUp(self):
        ClientModel.objects.create(
            phone='79999999999', 
            mobile_operator_code='999',
            tag='test'
            )

    def test_proper_client_creation(self):
        client = ClientModel.objects.get(phone='79999999999')
        self.assertEqual(client.mobile_operator_code, '999')

    def test_failure_client_creation(self):
        from django.core.exceptions import ValidationError
        client = ClientModel(
            phone='7999999999a', 
            mobile_operator_code='999',
            tag='test'
        )
        with self.assertRaises(ValidationError):
            if client.full_clean():
                client.save()
        
        self.assertEqual(ClientModel.objects.filter(phone='7999999999a').count(), 0)


class ClientModelDrfTestCase(TestCase):

    def test_post_bank(self):
        url = reverse('clients-list')
        data = {
            'phone': '78888888888',
            'mobile_operator_code': '777',
            'tag': 'drf',
            'timezone': 'Canada/Pacific'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ClientModel.objects.count(), 1)
        self.assertEqual(ClientModel.objects.get().phone, '78888888888')

    def test_patch_bank(self):
        url = reverse('clients-list')
        data = {
            'phone': '71111111111',
            'mobile_operator_code': '777',
            'tag': 'drf',
            'timezone': 'Canada/Pacific'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ClientModel.objects.count(), 1)
        self.assertEqual(ClientModel.objects.get().phone, '71111111111')

        url = reverse('clients-detail', args=(1,))
        import json 
        data = json.dumps({'phone': '72222222222'})
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(ClientModel.objects.get().phone, '72222222222')

    def test_delete_bank(self):
        url = reverse('clients-detail', args=(1,))
        response = self.client.delete(url)
        self.assertEqual(ClientModel.objects.count(), 0)