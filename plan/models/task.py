from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from plan.models.project import Project

TASK_STATUS = (
	(1, "Open"),
	(2, "In progress"),
	(3, "Stoped"),
	(4, "Testing"),
	(5, "Closed"),
)

class Task(models.Model):
	
	title = models.CharField(max_length=50, unique=True)
	user = models.ForeignKey(User, null=True, blank=True)
	project = models.ForeignKey(Project, related_name='+')
	progress = models.PositiveIntegerField()
	status = models.IntegerField(choices=TASK_STATUS, default=1)
	deadline = models.DateTimeField(auto_now=False, null=True, blank=True)
	date_added = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		app_label = 'plan'


class TaskAdmin(admin.ModelAdmin):
	
	list_display = ('title', 'user', 'progress', 'status', 'deadline', 'date_added')	
