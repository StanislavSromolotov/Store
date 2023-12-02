from django.db import models

from .customer import Customer


class Orders(models.Model):

    id = models.SmallAutoField(primary_key=True, unique=True)
    date = models.DateTimeField(blank=False)
    sum_total = models.IntegerField(blank=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.customer_id} {self.sum_total} {self.date}'
