from django.forms import ModelForm
from plan.models.project import Project

class ProjectForm(ModelForm):
	
	class Meta:
		model = Project
		fields = '__all__'

