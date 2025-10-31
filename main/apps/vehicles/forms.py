from django import forms
from .models import Veiculo, TipoVeiculo

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class TipoVeiculoForm(FormSettings):
    class Meta:
        model = TipoVeiculo
        fields = ['nome', 'descricao', 'ativo']
        labels = {
            'nome': 'Nome do tipo de veículo*',
            'descricao': 'Descrição',
            'ativo': 'Ativo'
        }
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class VeiculoAddForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(VeiculoAddForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Veiculo
        fields = ['tipo_veiculo', 'contrato', 'placa', 'situacao', 'statusPlaca']
        labels = {
            'tipo_veiculo': 'Tipo de Veículo*',
            'contrato': 'Contrato*',
            'placa': 'Placa*',
            'situacao': 'Situação',
            'statusPlaca': 'Status da Placa',
        }