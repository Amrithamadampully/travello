# Generated by Django 4.2.2 on 2023-06-16 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='owner',
        ),
    ]