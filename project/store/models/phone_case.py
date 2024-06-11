from django.db import models


class Phone_case(models.Model):
    id = models.SmallAutoField(primary_key=True, unique=True)
    image = models.ImageField(
        upload_to="store_images", blank=True, null=True, verbose_name="Image"
    )
    model = models.CharField(
        max_length=30, blank=False, help_text="модель чехла для телефона"
    )
    color = models.CharField(
        max_length=30, blank=False, help_text="цвет чехла"
    )
    material = models.CharField(
        max_length=30, blank=False, help_text="материал чехла"
    )
    price = models.IntegerField(blank=False)

    def __str__(self) -> str:
        return f"{self.model} {self.color} {self.material} {self.price}"
