from django.test import TestCase
from django.urls import reverse
from Restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='Menu 1', price=10.99, inventory=20)
        self.menu2 = Menu.objects.create(title='Menu 2', price=15.99, inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menus = Menu.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(menus))
