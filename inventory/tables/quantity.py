import django_tables2 as tables

from django_tables2 import RequestConfig
from django_tables2.utils import A

from inventory.models.quantity import Quantity

class QuantityTable(tables.Table):

	buttons = {
		'add':'QuantityFormCreateView',
	}


	code = tables.LinkColumn('QuantityFormUpdateView', args=[A('pk')])

	class Meta:

		template = 'templates/table.html'
		model = Quantity
