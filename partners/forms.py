from django import forms

from .models import Partners


class CreatePartner(forms.ModelForm):

    class Meta:
        model = Partners
        fields = ('Name', 'Surname', 'Email', 'Sponsor', 'Manager Name', 'Manager approve', 'CEO approve')
