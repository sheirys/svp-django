import django_tables2 as tables

from django_tables2 import RequestConfig
from django_tables2.utils import A

from plan.models.project import Project

class ProjectTable(tables.Table):

	buttons = {
		'add': 'ProjectFormCreateView',
	}

	class Meta:

		template = 'templates/table.html'
		model = Project
