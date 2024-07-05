# Generated by Django 4.1.13 on 2024-07-02 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('burgers', '0002_remove_burger_order'),
        ('drinks', '0002_remove_drink_order'),
        ('clients', '0001_initial'),
        ('pizzas', '0002_remove_pizza_order'),
        ('snacks', '0004_remove_snack_order'),
        ('orders', '0004_rename_burgers_order_burger_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='burger',
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='drink',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='order',
            name='snack',
        ),
        migrations.AddField(
            model_name='order',
            name='burger',
            field=models.ManyToManyField(blank=True, to='burgers.burger'),
        ),
        migrations.AddField(
            model_name='order',
            name='drink',
            field=models.ManyToManyField(blank=True, to='drinks.drink'),
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ManyToManyField(blank=True, to='pizzas.pizza'),
        ),
        migrations.AddField(
            model_name='order',
            name='snack',
            field=models.ManyToManyField(blank=True, to='snacks.snack'),
        ),
    ]
