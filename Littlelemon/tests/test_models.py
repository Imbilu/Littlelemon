from django.test import TestCase
from Restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Icecream', price=8, inventory=100)
        self.assertEqual(str(item), 'Icecream: 8')