import django_tables2 as tables

from django_tables2 import RequestConfig

from inventory.models.product import Product

class ProductTable(tables.Table):

	class Meta:

		template = 'templates/table.html'
		model = Product
