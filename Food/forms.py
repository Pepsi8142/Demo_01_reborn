from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        # fields = ['item_name', 'item_description', 'item_price', 'item_quantity', 'item_image']
