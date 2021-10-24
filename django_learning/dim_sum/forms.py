from django import forms
from .models import DimSumItem


class AddItemForm(forms.ModelForm):

    """From DimSumItem model, designate the fields that contributors
    can fill out in this form.
    """

    item_name = forms.CharField(widget=forms.TextInput(attrs={
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

    class Meta:

        model = DimSumItem
        fields = [
            'item_name',
            'description',
            'normal_price',
            'history'
        ]

    def clean_item_name(self, *args, **kwargs):
        """Raise validation error if item name contain invalid words."""
        item_name = self.cleaned_data.get("item_name")
        if "dim sum" in item_name:
            raise forms.ValidationError("This is not a valid item name")
        if "garbage" in item_name:
            raise forms.ValidationError("This is not a valid item name")
        return item_name


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