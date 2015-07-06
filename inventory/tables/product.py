import django_tables2 as tables

from django_tables2 import RequestConfig
from django_tables2.utils import A

from inventory.models.product import Product

class ProductTable(tables.Table):

	buttons = {
		'add': 'ProductFormView',
		'export': 'ProductFormView',
	}

	model = tables.LinkColumn('ProductFormView', args=[A('pk')])

	class Meta:

		template = 'templates/table.html'
		model = Product
