# Generated by Django 4.2.2 on 2023-06-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_delete_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('nam', models.CharField(max_length=200)),
                ('des', models.TextField()),
            ],
        ),
    ]
