from django.contrib import admin

from inventory.models.product import Product, ProductAdmin
from inventory.models.warehouse import Warehouse, WarehouseAdmin
from inventory.models.quantity import Quantity, QuantityAdmin

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Quantity, QuantityAdmin)
