from django.db import models


class Phone_case(models.Model):
    id = models.SmallAutoField(primary_key=True, unique=True)
    image = models.ImageField(
        upload_to="store_images",
        blank=True,
        null=True,
        verbose_name="Картинка",
    )
    model = models.CharField(
        max_length=30, blank=False, verbose_name="Модель чехла для телефона"
    )
    color = models.CharField(
        max_length=30, blank=False, verbose_name="Цвет чехла"
    )
    material = models.CharField(
        max_length=30, blank=False, verbose_name="Материал чехла"
    )
    price = models.IntegerField(blank=False)
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание"
    )

    def __str__(self) -> str:
        return f"{self.model} {self.color} {self.material} {self.price}"
