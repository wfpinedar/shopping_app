import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from shop.models import Order, User
from shop.serializers import OrderSerializer
from shop.views import OrderViewSet

client = Client()

class AuthTests(TestCase):
    def setUp(self):
        user = User.objects.create(username='test', email='test@test.com', is_staff=True, is_superuser=True)
        user.set_password('test123')
        user.save()
    
    def test_failed_login(self):
        # failed login API response
        login=client.login(username='fail', password='fail123')
        self.assertFalse(login)

    def test_success_login(self):
        # success login API response
        login=client.login(username='test', password='test123')
        self.assertTrue(login)
    

class OrderTests(TestCase):
    """ Test module to GET and orders API"""

    def setUp(self):
        user = User.objects.create(username='test', email='test@test.com', is_staff=True, is_superuser=True)
        user.set_password('test123')
        user.save()
        self.user = user
        login=client.login(username='test', password='test123')
        self.assertTrue(login)
        Order.objects.create(status="A", user=user)
        Order.objects.create(status="I", user=user)
        Order.objects.create(status="A", user=user)
    
    def test_get_all_orders(self):
        # get API response
        response = client.get(reverse('order'))
        # get data from db
        orders = Order.objects.all()
        for o in orders:
            print(o.id)
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
