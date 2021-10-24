from django import forms
from .models import OwnerUpdate


class UpdateCreateForm(forms.ModelForm):
    class Meta:
        model = OwnerUpdate
        fields = [
            'update_title',
            'content',
            'update_type'
        ]