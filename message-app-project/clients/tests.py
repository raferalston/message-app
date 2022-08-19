from django.test import TestCase

from .models import ClientModel


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