from django import forms
from .models import Lance

class LanceForm(forms.ModelForm):
    class Meta:
        model = Lance
        fields = ['valor'] 