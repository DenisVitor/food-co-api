# Generated by Django 4.1.13 on 2024-07-02 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_order_burger_alter_order_client_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='burger',
            new_name='burgers',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='drink',
            new_name='drinks',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='pizza',
            new_name='pizzas',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='snack',
            new_name='snacks',
        ),
    ]
