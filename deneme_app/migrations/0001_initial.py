# Generated by Django 3.1.5 on 2021-07-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=10)),
            ],
        ),
    ]