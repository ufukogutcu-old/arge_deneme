from django.core.management.base import BaseCommand, CommandError
from deneme_app.models import Item, MyUser
import random
import string


class Command(BaseCommand):
    help = 'Clears all items and Generates specified amount of items per user'

    def add_arguments(self, parser):
        parser.add_argument('number_of_items', type=int)

    def handle(self, *args, **options):
        number_of_items = options['number_of_items']
        items = Item.objects.all()
        # for item in items:
        #     item.delete()
        used_names = []
        color_choices = ['red', 'blue', 'green', 'yellow', 'black', 'pink']
        letters = string.ascii_letters
        for user in MyUser.objects.all():
            for i in range(number_of_items):
                name = ''.join(random.choice(letters) for i in range(10))
                while name in used_names:
                    name = ''.join(random.choice(letters) for i in range(10))
                size = random.randint(1, 50)
                color = color_choices[random.randint(0, len(color_choices) - 1)]
                item = Item(
                    name=name,
                    size=size,
                    color=color,
                    creator=user
                )
                used_names.append(name)
                print(item)
                # item.save()
        self.stdout.write('Successfully created {} items for each user'.format(str(number_of_items)))
