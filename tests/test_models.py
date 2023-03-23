from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice creame",price=33,inventory=33)
        itemstr = item.get_item()
        self.assertEqual(itemstr,"Ice creame : 33")