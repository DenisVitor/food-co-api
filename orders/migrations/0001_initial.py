# Generated by Django 5.0.6 on 2024-06-27 13:39

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('delivering_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
        ),
    ]
