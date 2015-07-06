from django.http import HttpResponse
from django_tables2 import RequestConfig, SingleTableView
from django.contrib.auth.decorators import login_required
from django.views import generic

from inventory.models.product import Product
from inventory.tables.product import ProductTable

#@login_required
class ProductListView(SingleTableView, generic.ListView):

	model = Product
	template_name = 'inventory/table.html'
	table_class = ProductTable
