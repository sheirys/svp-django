import django_tables2 as tables

from django_tables2 import RequestConfig

from inventory.models.quantity import Quantity

class QuantityTable(tables.Table):

	buttons = {
		'add':'QuantityFormView',
	}

	class Meta:

		template = 'templates/table.html'
		model = Quantity
