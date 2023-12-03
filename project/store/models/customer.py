from django.db import models


class Customer(models.Model):
    id = models.SmallAutoField(primary_key=True, unique=True)
    name = models.CharField(
        max_length=30, blank=False, help_text="Введите имя пользователя"
    )
    phone = models.CharField(
        max_length=12, blank=False, unique=True, help_text="Введите номер телефона"
    )
    address = models.CharField(max_length=30, help_text="Введите адрес проживания")
    email = models.CharField(
        max_length=30, unique=True, help_text="Введите электронную почту"
    )

    def __str__(self):
        return f"Customer: {self.name} {self.phone}"
