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
    

class Phone(models.Model):

    id = models.SmallAutoField(primary_key=True)
    
    PHONE_TYPE = [
        ('smartphone', 'Смартфон'), 
        ('push_button_telephone', 'Кнопочный телефон')
        ] 
    type = models.CharField(max_length=30, blank=False, choices=PHONE_TYPE)

    PHONE_OS = [
        ('android', 'Android'), 
        ('ios', 'iOS')
        ]
    os = models.CharField(max_length=30, blank=False, choices=PHONE_OS)
    version_os = models.CharField(max_length=30, blank=False)
    phone_model = models.CharField(max_length=30, blank=False)
    cpu = models.CharField(max_length=30, blank=False, help_text='процессор')
    number_cores = models.IntegerField(blank=False, help_text='кол-во ядер поцессора')
    processor_power = models.IntegerField(blank=False, help_text='разрядность процессора')
    battery_type = models.CharField(max_length=20, blank=False, help_text='тип аккумулятора')
    battery_capasity = models.IntegerField(blank=False, help_text='емкость аккумулятора')
    color = models.CharField(max_length=30, blank=False, help_text='цвет модели телефона')
    screen_size = models.CharField(max_length=15, blank=False, help_text='размер экрана')
    camera = models.CharField(max_length=30, blank=False, help_text='кол-во точек матрицы')
    number_cameras = models.IntegerField(blank=False, help_text='цвет модели телефона')
    number_sim_сards = models.IntegerField(blank=False, help_text='кол-во SIM-карт')
    memory_card_support = models.CharField(max_length=3, blank=False, help_text='поддержка дополнительной карты памяти') 
    manufacturer = models.CharField(max_length=20, blank=False, help_text='страна производства')
    price = models.IntegerField(blank=False, help_text='стоимость телефона')
    release_date = models.DateField(blank=False)

    class Meta():
        db_table = 'phone'
        db_table_comment = 'table about phone'

    def __str__(self) -> str:
        return f'{self.phone_model} {self.color} {self.price}'
    
class Phone_case(models.Model):

    id = models.SmallAutoField(primary_key=True)
    model = models.CharField(max_length=30, blank=False, help_text='модель чехла для телефона')
    color = models.CharField(max_length=30, blank=False, help_text='цвет чехла')
    material = models.CharField(max_length=30, blank=False, help_text='материал чехла')
    price = models.IntegerField(blank=False)

    class Meta():
        db_table = 'phone case'
        db_table_comment = 'table about phone case'

    def __str__(self) -> str:
        return f'{self.model} {self.color} {self.material} {self.price}'
    