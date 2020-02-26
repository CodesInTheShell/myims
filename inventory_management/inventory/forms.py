from django import forms

from .models import *

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('sku', 'description', 'onhand')

		widgets = {
          'description': forms.Textarea(attrs={'rows':2, 'cols':30}),
        }


class IncomingItemForm(forms.Form):
    receiver = forms.CharField(label='Receiver', max_length=100)
    sender = forms.CharField(label='Sender', max_length=100)