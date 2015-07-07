from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django_tables2 import RequestConfig, SingleTableView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from plan.models.task import Task
from plan.tables.task import TaskTable
from plan.forms.task import TaskForm

#@login_required
class TaskListView(SingleTableView, ListView):
	model = Task
	template_name = 'inventory/table.html'
	table_class = TaskTable

class TaskFormCreateView(CreateView):
	model = Task
	template_name = 'inventory/form.html'
	form_class = TaskForm
	success_url = reverse_lazy('TaskListView')

class TaskFormUpdateView(UpdateView):
	model = Task
	template_name = 'inventory/form.html'
	form_class = TaskForm
	success_url = reverse_lazy('TaskListView')
