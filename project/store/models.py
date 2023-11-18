from django.db import models

class Phone(models.Model):
    APPLE = 'AP'
    ANDROID = 'AD'

    MANUFACTURER = [
        (APPLE, 'Apple'),
        (ANDROID, 'Android'),
    ]

    SMARTPHONE = 'SM'
    MOBILE_PHONE = 'MF'

    TYPE = [
        (SMARTPHONE, 'smartphone'),
        (MOBILE_PHONE, 'mobile_phone'),
    ]

    IOS = 'iOS'
    SYSTEM = [
        (IOS, 'iOS'),
        (ANDROID, 'Android'),
    ]

    manufacturer = models.CharField(max_length=2, choices=MANUFACTURER, default=APPLE)
    type = models.CharField(max_length=2, choices=TYPE, default=SMARTPHONE)
    system = models.CharField(max_length=7, choices=SYSTEM, default=IOS)
    price = models.IntegerField(default=0)
