# Generated by Django 4.1.13 on 2024-07-02 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_burger_order_burgers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='burgers',
            new_name='burger',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='drinks',
            new_name='drink',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='pizzas',
            new_name='pizza',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='snacks',
            new_name='snack',
        ),
    ]
