from django.http import HttpResponse
from django_tables2 import RequestConfig, SingleTableView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from inventory.models.product import Product
from inventory.forms.product import ProductForm
from inventory.tables.product import ProductTable

#@login_required
class ProductListView(SingleTableView, ListView):
	model = Product
	template_name = 'inventory/table.html'
	table_class = ProductTable

class ProductDetailView(DetailView):
	model = Product
	template_name = 'inventory/detail.html'

class ProductFormCreateView(CreateView):
	model = Product
	template_name = 'inventory/form.html'
	form_class = ProductForm

class ProductFormUpdateView(UpdateView):
	model = Product
	template_name = 'inventory/form.html'
	form_class = ProductForm
	success_url = '#'

