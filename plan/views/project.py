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

from plan.models.project import Project
from plan.tables.project import ProjectTable

#@login_required
class ProjectListView(SingleTableView, ListView):
	model = Project
	template_name = 'inventory/table.html'
	table_class = ProjectTable

"""
class ProductDetailView(DetailView):
	model = Product
	template_name = 'inventory/detail.html'

class ProductFormCreateView(CreateView):
	model = Product
	template_name = 'inventory/form.html'
	form_class = ProductForm
	success_url = reverse_lazy('ProductListView')

class ProductFormUpdateView(UpdateView):
	model = Product
	template_name = 'inventory/form.html'
	form_class = ProductForm
	success_url = reverse_lazy('ProductListView')
"""			
