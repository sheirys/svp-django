from django.db import models
from django.contrib import admin

class Warehouse(models.Model):
	name = models.CharField(max_length=50)
	enabled = models.BooleanField(default=True)
	date_added = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

	class Meta:
		app_label = 'inventory'


class WarehouseAdmin(admin.ModelAdmin):
	list_display = ('name', 'enabled', 'date_added')
