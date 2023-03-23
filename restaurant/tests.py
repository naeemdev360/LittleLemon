from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice creame",price=33,inventroy=6)
        itemstr = item.title
        item_inv = item.inventroy
        self.assertEqual(itemstr,"Ice creame")
        self.assertEqual(item_inv,6)