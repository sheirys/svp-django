from django.http import HttpResponse
from django_tables2 import RequestConfig, SingleTableView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import FormView

from inventory.models.quantity import Quantity
from inventory.tables.quantity import QuantityTable
from inventory.forms.quantity import QuantityForm

#@login_required
class QuantityListView(SingleTableView, ListView):

	model = Quantity
	template_name = 'inventory/table.html'
	table_class = QuantityTable


class QuantityFormView(FormView):
	template_name = 'inventory/form.html'
	form_class = QuantityForm

