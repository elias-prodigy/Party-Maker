from django import forms

from .models import Partners


class CreatePartner(forms.ModelForm):
    class Meta:
        model = Partners
        fields = ('name', 'surname', 'email', 'sponsor', 'manager_name')

