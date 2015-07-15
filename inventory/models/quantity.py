from django.db import models
from django.contrib import admin

from inventory.models.product import Product
from inventory.models.warehouse import Warehouse

class Quantity(models.Model):

	code = models.CharField(max_length=50, unique=True)
	warehouse = models.ForeignKey(Warehouse)
	closed = models.BooleanField(default=False)
	comment = models.TextField(null=True, blank=True)
	date_added = models.DateTimeField(auto_now=True)

	class Meta:
		app_label = 'inventory'


class QuantityProduct(models.Model):

	code = models.ForeignKey(Quantity, related_name='+')
	model = models.ForeignKey(Product, related_name='+')
	quantity = models.IntegerField()
	date_added = models.DateTimeField(auto_now=True)

	class Meta:
		app_label = 'inventory'


class QuantityProductAdmin(admin.ModelAdmin):
	list_display = ('model', 'quantity', 'date_added')

class QuantityAdmin(admin.ModelAdmin):
	list_display = ('warehouse', 'date_added')
