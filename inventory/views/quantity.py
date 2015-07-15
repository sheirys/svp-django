from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django_tables2 import RequestConfig, SingleTableView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from inventory.models.quantity import Quantity
from inventory.tables.quantity import QuantityTable
from inventory.forms.quantity import QuantityForm
from inventory.forms.quantity import QuantityProductFormset

#@login_required
class QuantityListView(SingleTableView, ListView):

	model = Quantity
	template_name = 'inventory/table.html'
	table_class = QuantityTable

class QuantityDetailView(DetailView):
	
	model = Quantity
	template_name = 'inventory/quantity/detail.html'

class QuantityFormCreateView(CreateView):

	model = Quantity
	template_name = 'inventory/form.html'
	form_class = QuantityForm
	success_url = reverse_lazy('QuantityListView')

	def get_context_data(self, **kwargs):
		context = super(QuantityFormCreateView,self).get_context_data(**kwargs)
		if self.request.POST:
			context['formset'] = QuantityProductFormset(self.request.POST)
		else:
			context['formset'] = QuantityProductFormset()
		return context

	def form_valid(self, form):
		context = self.get_context_data()
		formset = context['formset']
		if formset.is_valid():
			self.object = form.save()
			formset.instance = self.object
			formset.save()
			return redirect(self.success_url)
		else:
			return self.render_to_response(self.get_context_data(form=form))

class QuantityFormUpdateView(UpdateView):

	model = Quantity
	template_name = 'inventory/form.html'
	form_class = QuantityForm
	success_url = reverse_lazy('QuantityListView')

	def get_context_data(self, **kwargs):
		context = super(QuantityFormUpdateView,self).get_context_data(**kwargs)
		context['formset'] = QuantityProductFormset(instance=self.object)
		return context

