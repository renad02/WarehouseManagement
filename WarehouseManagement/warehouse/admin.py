from django.contrib import admin
from .models import Products
from .models import Customers
from .models import Suppliers
from .models import Order
from .models import Invoice
from .models import Report
from .models import Warehouse
from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Suppliers)
admin.site.register(Order)
admin.site.register(Invoice)
admin.site.register(Report)
admin.site.register(Warehouse)
