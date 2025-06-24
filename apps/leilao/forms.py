from django import forms
from .models import Leilao
from apps.produto.models import Produto 

class LeilaoForm(forms.ModelForm):
    class Meta:
        model = Leilao
        fields = [
            'leiloeiro',
            'produtos',
            'data_inicio',
            'data_fim',
        ]
        widgets = {
            'data_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'data_fim': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'produtos': forms.SelectMultiple(attrs={'class': 'form-control'}), 
        }
        labels = {
            'leiloeiro': 'Leiloeiro Responsável',
            'produtos': 'Produtos do Leilão',
            'data_inicio': 'Data e Hora de Início',
            'data_fim': 'Data e Hora de Término',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.DateTimeInput, forms.SelectMultiple)):
                field.widget.attrs.update({'class': 'form-control'})
        self.fields['produtos'].queryset = Produto.objects.filter(status='DISPONIVEL')

        