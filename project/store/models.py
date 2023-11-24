from django.db import models


class Customer(models.Model):

    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, help_text='Введите имя пользователя')
    phone = models.CharField(max_length=12, blank=False, unique=True, help_text='Введите номер телефона')
    address = models.CharField(max_length=30, help_text='Введите адрес проживания')
    email = models.CharField(max_length=30, unique=True, help_text='Введите электронную почту')


    class Meta():
        db_table = 'customer'
        db_table_comment = 'table about customer'

    def __str__(self):
        return f'Customer: {self.name} {self.phone}'
    
class Orders(models.Model):

    id = models.SmallAutoField(primary_key=True)
    date = models.DateTimeField(blank=False)
    sum_total = models.IntegerField(blank=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta():
        db_table = 'orders'
        db_table_comment = 'table about orders'

    def __str__(self) -> str:
        return f'{self.customer_id} {self.sum_total} {self.date}'