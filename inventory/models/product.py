from django.db import models
from django.contrib import admin

class Product(models.Model):
	
	model = models.CharField(max_length=50, unique=True)
	total_quantity = models.IntegerField()
	accounting = models.CharField(max_length=6, default="FILO")
	enabled = models.BooleanField(default=True)

	def __str__(self):
		return self.model

	class Meta:
		app_label = 'inventory'


class ProductAdmin(admin.ModelAdmin):
	
	list_display = ('model', 'total_quantity', 'accounting', 'enabled')	
