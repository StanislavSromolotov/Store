from django.db import models

from .phone import Phone
from .orders import Orders


class Orders_phone(models.Model):

    orders_fk = models.ManyToManyField(Orders)
    phone_fk = models.ManyToManyField(Phone)
