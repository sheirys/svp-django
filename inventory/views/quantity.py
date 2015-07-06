from django.http import HttpResponse
from django_tables2 import RequestConfig, SingleTableView
from django.contrib.auth.decorators import login_required
from django.views import generic

from inventory.models.quantity import Quantity
from inventory.tables.quantity import QuantityTable

#@login_required
class QuantityListView(SingleTableView, generic.ListView):

	model = Quantity
	template_name = 'inventory/table.html'
	table_class = QuantityTable
