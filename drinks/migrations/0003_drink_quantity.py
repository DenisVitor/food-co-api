# Generated by Django 3.2.25 on 2024-07-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0002_remove_drink_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='quantity',
            field=models.IntegerField(default=1, max_length=20),
        ),
    ]
