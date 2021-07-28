from django.test import TestCase
from deneme_app.models import Item


class ItemTest(TestCase):
    def test_create_item(self):
        number_of_items = 40
        for i in range(number_of_items):
            Item.objects.create(name=str(i), size=10, color='red')
        self.assertEqual(number_of_items, Item.objects.count())

        item = Item.objects.first()
        self.assertEqual(item.name, '0')
        self.assertEqual(item.size, 10)
        self.assertEqual(item.color, 'red')

    def test_delete_item(self):
        item = Item.objects.create(name='a', size=10, color='red')
        self.assertEqual(Item.objects.count(), 1)

        item.delete()
        self.assertEqual(Item.objects.count(), 0)

    def test_edit_item(self):
        Item.objects.create(name='a', size=10, color='red')
        item = Item.objects.first()
        item.name = 'b'
        item.size = 20
        item.color = 'blue'
        self.assertEqual(item.name, 'b')
        self.assertEqual(item.size, 20)
        self.assertEqual(item.color, 'blue')
