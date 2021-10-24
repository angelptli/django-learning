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
    item_name    = forms.CharField(widget=forms.TextInput(attrs={
                                          "placeholder": "Dim Sum Item"}))
    description  = forms.CharField(
                         required=False,
                         widget=forms.Textarea(
                                attrs={
                                    "class": "new-class-name two",
                                    "placeholder": "Dim sum's description",
                                    "rows": 20,
                                    "cols": 120
                                }))
    normal_price = forms.DecimalField(required=False)
    history      = forms.CharField(required=False)
    tasty        = forms.CheckboxInput()