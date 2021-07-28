from django.test import TestCase
from deneme_app.models import Item
from rest_framework.test import APIClient, APITestCase
from deneme_app.serializers import ItemSerializer


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


class APITest(APITestCase):
    username = 'ufukogutcu'
    password = 'Ufuk2007'

    def test_get_item(self):
        Item.objects.create(name='a', size=10, color='red')
        Item.objects.create(name='b', size=20, color='blue')
        client = APIClient()
        client.login(username=self.username, password=self.password)
        response = client.get('/api/items/', content_type='json')
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(len(data), 2)
        item_1 = data[0]
        self.assertEqual(item_1.get('name'), 'a')
        self.assertEqual(item_1.get('size'), 10)
        self.assertEqual(item_1.get('color'), 'red')
        item_2 = data[1]
        self.assertEqual(item_2.get('name'), 'b')
        self.assertEqual(item_2.get('size'), 20)
        self.assertEqual(item_2.get('color'), 'blue')
        client.logout()

    def test_post_item(self):
        client = APIClient()
        client.login(username=self.username, password=self.password)
        item = Item.objects.create(name='a', size=30, color='red')
        data = ItemSerializer(item).data
        response = client.post('/api/items/', data, format='json')
        self.assertEqual(Item.objects.first().name, 'a')
        self.assertEqual(Item.objects.first().size, 30)
        self.assertEqual(Item.objects.first().color, 'red')
        client.logout()

    def test_delete_item(self):
        client = APIClient()
        client.login(username=self.username, password=self.password)
        item = Item.objects.create(name='a', size=10, color='red')
        self.assertEqual(Item.objects.count(), 1)
        response = client.delete('/api/items/a/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Item.objects.count(), 0)

    def test_edit_item(self):
        client = APIClient()
        client.login(username=self.username, password=self.password)
        item = Item.objects.create(name='a', size=10, color='red')
        data = {'name': 'a', 'size': 10, 'color': 'blue'}
        response = client.put('/api/items/a/', data)
        self.assertEqual(Item.objects.first().color, 'blue')
        data = {'name': 'a', 'size': 20, 'color': 'blue'}
        response = client.put('/api/items/a/', data)
        self.assertEqual(Item.objects.first().size, 20)
        client.logout()
