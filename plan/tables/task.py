import django_tables2 as tables

from django_tables2 import RequestConfig
from django_tables2.utils import A

from plan.models.task import Task

class TaskTable(tables.Table):

	buttons = {
		'add': 'TaskFormCreateView',
	}

	class Meta:

		template = 'templates/table.html'
		model = Task
