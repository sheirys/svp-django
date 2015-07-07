from django.core.urlresolvers import reverse_lazy
from django_tables2 import RequestConfig, SingleTableView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from inventory.models.quantity import Quantity
from inventory.tables.quantity import QuantityTable
from inventory.forms.quantity import QuantityForm

#@login_required
class QuantityListView(SingleTableView, ListView):

	model = Quantity
	template_name = 'inventory/table.html'
	table_class = QuantityTable

class QuantityFormCreateView(CreateView):
	model = Quantity
	template_name = 'inventory/form.html'
	form_class = QuantityForm
	success_url = reverse_lazy('QuantityListView')

class QuantityFormUpdateView(UpdateView):
	model = Quantity
	template_name = 'inventory/form.html'
	form_class = QuantityForm
	success_url = reverse_lazy('QuantityListView')

