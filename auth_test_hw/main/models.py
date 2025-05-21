from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Уникальный email
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Необязательное поле

    USERNAME_FIELD = 'email'  # Используем email как основное поле для входа
    REQUIRED_FIELDS = []  # Убираем стандартные поля (username)

    def __str__(self):
        return self.email