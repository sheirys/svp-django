from django.conf.urls import url

from inventory.views.product import ProductListView
from inventory.views.product import ProductFormView
from inventory.views.quantity import QuantityListView
from inventory.views.quantity import QuantityFormView

urlpatterns = [
	url(r'^product/$', ProductListView.as_view(), name='InventoryProduct'), 
	url(r'^product/edit', ProductFormView.as_view(), name='InventoryProductAdd'),
	url(r'^quantity/$', QuantityListView.as_view(), name='InventoryQuantity'), 
	url(r'^quantity/edit', QuantityFormView.as_view(), name='InventoryQuantityAdd'), 
]
