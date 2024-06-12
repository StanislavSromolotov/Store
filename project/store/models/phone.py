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
    cpu = models.CharField(
        max_length=30, blank=False, verbose_name="Процессор"
    )
    number_cores = models.IntegerField(
        blank=False, verbose_name="Кол-во ядер поцессора"
    )
    processor_power = models.IntegerField(
        blank=False, verbose_name="Разрядность процессора"
    )
    battery_type = models.CharField(
        max_length=20, blank=False, verbose_name="Тип аккумулятора"
    )
    battery_capasity = models.IntegerField(
        blank=False, verbose_name="Емкость аккумулятора"
    )
    color = models.CharField(
        max_length=30, blank=False, verbose_name="Цвет модели телефона"
    )
    screen_size = models.CharField(
        max_length=15, blank=False, verbose_name="Размер экрана"
    )
    camera = models.CharField(
        max_length=30, blank=False, verbose_name="Кол-во точек матрицы"
    )
    number_cameras = models.IntegerField(
        blank=False, verbose_name="Цвет модели телефона"
    )
    number_sim_cards = models.IntegerField(
        blank=False, verbose_name="Кол-во SIM-карт"
    )
    memory_card_support = models.CharField(
        max_length=3,
        blank=False,
        verbose_name="Поддержка дополнительной карты памяти",
    )
    manufacturer = models.CharField(
        max_length=20, blank=False, verbose_name="Страна производства"
    )
    price = models.IntegerField(blank=False, verbose_name="Стоимость")
    release_date = models.DateField(blank=False)
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание"
    )

    def __str__(self) -> str:
        return f"{self.phone_model} {self.color} {self.price}"
