import django_tables2 as tables

from django_tables2 import RequestConfig
from django_tables2.utils import A

from inventory.models.product import Product

class ProductTable(tables.Table):

	buttons = {
		'add': 'ProductFormCreateView',
		'export': 'ProductFormCreateView',
	}

	id = tables.TemplateColumn('<input type="checkbox" value="{{ record.pk }}" /> {{ record.pk }}', verbose_name="ID")
	model = tables.LinkColumn('ProductFormUpdateView', args=[A('pk')])

	class Meta:

		template = 'templates/table.html'
		model = Product
