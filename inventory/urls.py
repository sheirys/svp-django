from django.conf.urls import url

from inventory.views.product import ProductListView
from inventory.views.product import ProductFormUpdateView
from inventory.views.product import ProductFormCreateView
from inventory.views.product import ProductDetailView
from inventory.views.quantity import QuantityListView
from inventory.views.quantity import QuantityFormView

urlpatterns = [
	url(r'^product/$', ProductListView.as_view(), name='ProductListView'), 
	url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='ProductDetailView'),
	url(r'^product/(?P<pk>\d+)/edit/$', ProductFormUpdateView.as_view(), name='ProductFormUpdateView'),
	url(r'^product/add/', ProductFormCreateView.as_view(), name='ProductFormCreateView'),
	url(r'^quantity/$', QuantityListView.as_view(), name='QuantityListView'), 
	url(r'^quantity/edit', QuantityFormView.as_view(), name='QuantityFormView'), 
]
