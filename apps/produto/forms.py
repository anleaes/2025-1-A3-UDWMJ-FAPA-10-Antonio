from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome',
            'descricao',
            'valor_inicial',
            'imagem',
            'tipo',
            'modalidade',
            'local',
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}), 
            'valor_inicial': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição Detalhada',
            'valor_inicial': 'Valor Inicial do Leilão',
            'imagem': 'Imagem do Produto',
            'tipo': 'Tipo de Produto',
            'modalidade': 'Modalidade do Leilão',
        }
        help_texts = {
            'valor_inicial': 'O valor mínimo para iniciar o leilão.',
            'imagem': 'Faça upload de uma imagem clara do produto.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea, forms.NumberInput, forms.Select, forms.FileInput)):
                field.widget.attrs.update({'class': 'form-control'})
            if field_name == 'imagem':
                field.widget.attrs.update({'class': 'form-control-file'})