from django.forms import ModelForm
from inventory.models.product import Product

class ProductForm(ModelForm):
	
	class Meta:
		model = Product


