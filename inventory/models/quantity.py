from django.db import models
from django.contrib import admin

from inventory.models.product import Product
from inventory.models.warehouse import Warehouse

class Quantity(models.Model):

	code = models.CharField(max_length=50, unique=True)
	model = models.ForeignKey(Product, related_name='+')
	warehouse = models.ForeignKey(Warehouse)
	quantity = models.IntegerField()
	closed = models.BooleanField(default=False)
	date_added = models.DateTimeField(auto_now=True)

	class Meta:
		app_label = 'inventory'

class QuantityAdmin(admin.ModelAdmin):
	list_display = ('model', 'warehouse', 'quantity', 'date_added')
