from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name','email', 'date_of_birth', 'phone_number','address','enrolled_programs']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'enrolled_programs': forms.CheckboxSelectMultiple(),
        }
