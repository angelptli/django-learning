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


class RawItemForm(forms.Form):
    item_name    = forms.CharField()
    description  = forms.CharField(required=False)
    normal_price = forms.DecimalField(required=False)
    history      = forms.CharField(required=False)
    tasty        = forms.CheckboxInput()