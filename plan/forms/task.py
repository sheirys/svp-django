from django.forms import ModelForm
from plan.models.task import Task

class TaskForm(ModelForm):
	
	class Meta:
		model = Task
		fields = '__all__'

