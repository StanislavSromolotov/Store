from django.db import models


PHONE_TYPE = [
    ("smartphone", "Смартфон"),
    ("push_button_telephone", "Кнопочный телефон"),
]

PHONE_OS = [("android", "Android"), ("ios", "iOS")]


class Phone(models.Model):
    id = models.SmallAutoField(primary_key=True, unique=True)
    image = models.ImageField(
        upload_to="store_images", blank=True, null=True, verbose_name="Image"
    )
    type = models.CharField(max_length=30, blank=False, choices=PHONE_TYPE)
    os = models.CharField(max_length=30, blank=False, choices=PHONE_OS)
    version_os = models.CharField(max_length=30, blank=False)
    phone_model = models.CharField(max_length=30, blank=False)
    cpu = models.CharField(max_length=30, blank=False, help_text="процессор")
    number_cores = models.IntegerField(
        blank=False, help_text="кол-во ядер поцессора"
    )
    processor_power = models.IntegerField(
        blank=False, help_text="разрядность процессора"
    )
    battery_type = models.CharField(
        max_length=20, blank=False, help_text="тип аккумулятора"
    )
    battery_capasity = models.IntegerField(
        blank=False, help_text="емкость аккумулятора"
    )
    color = models.CharField(
        max_length=30, blank=False, help_text="цвет модели телефона"
    )
    screen_size = models.CharField(
        max_length=15, blank=False, help_text="размер экрана"
    )
    camera = models.CharField(
        max_length=30, blank=False, help_text="кол-во точек матрицы"
    )
    number_cameras = models.IntegerField(
        blank=False, help_text="цвет модели телефона"
    )
    number_sim_cards = models.IntegerField(
        blank=False, help_text="кол-во SIM-карт"
    )
    memory_card_support = models.CharField(
        max_length=3,
        blank=False,
        help_text="поддержка дополнительной карты памяти",
    )
    manufacturer = models.CharField(
        max_length=20, blank=False, help_text="страна производства"
    )
    price = models.IntegerField(blank=False, help_text="стоимость телефона")
    release_date = models.DateField(blank=False)

    def __str__(self) -> str:
        return f"{self.phone_model} {self.color} {self.price}"
