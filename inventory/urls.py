from django.conf.urls import url

from inventory.views.product import ProductListView
from inventory.views.quantity import QuantityListView

urlpatterns = [
	url(r'^products/', ProductListView.as_view(), name='InventoryProducts'), 
	url(r'^quantities/', QuantityListView.as_view(), name='InventoryQuantities'), 
]
