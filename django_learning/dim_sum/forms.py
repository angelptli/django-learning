from django import forms
from .models import DimSumItem


class AddItemForm(forms.ModelForm):

    """From DimSumItem model, designate the fields that contributors
    can fill out in this form.
    """

    class Meta:

        model = DimSumItem
        fields = [
            'item_name',
            'description',
            'normal_price',
            'history'
        ]
