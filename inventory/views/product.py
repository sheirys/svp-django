from django.http import HttpResponse
from django_tables2 import RequestConfig, SingleTableView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView

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

class ProductFormView(FormView):
	template_name = 'inventory/form.html'
	form_class = ProductForm
	success_url = '#'

	def form_valid(self, form):
		form.save()
		return super(ProductFormView, self).form_valid(form)

