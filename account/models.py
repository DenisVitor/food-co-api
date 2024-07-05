from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Account(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)
