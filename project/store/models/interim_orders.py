from django.db import models

from .phone import Phone
from .phone_case import Phone_case

class Interim_orders(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    phone_case = models.ForeignKey(Phone_case, on_delete=models.CASCADE)
