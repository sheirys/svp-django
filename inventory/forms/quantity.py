from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from inventory.models.quantity import Quantity
from inventory.models.quantity import QuantityProduct

class QuantityForm(ModelForm):
	class Meta:
		model = Quantity
		fields = '__all__'

QuantityProductFormset = inlineformset_factory(Quantity,QuantityProduct,
	fields=('model', 'quantity'),
	extra=1)

