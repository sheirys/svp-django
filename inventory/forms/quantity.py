from django.forms import ModelForm
from inventory.models.quantity import Quantity

class QuantityForm(ModelForm):
	class Meta:
		model = Quantity
		fields = '__all__'
