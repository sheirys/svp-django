from django.db import models
from django.contrib import admin

class Project(models.Model):
	
	name = models.CharField(max_length=50, unique=True)
	enabled = models.BooleanField(default=True)
	date_added = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		app_label = 'plan'


class ProjectAdmin(admin.ModelAdmin):
	
	list_display = ('name', 'enabled', 'date_added')	
