from django.contrib import admin
from store.models.customer import Customer
from store.models.orders import Orders
from store.models.phone import Phone
from store.models.phone_case import Phone_case


admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Phone_case)
admin.site.register(Phone)
