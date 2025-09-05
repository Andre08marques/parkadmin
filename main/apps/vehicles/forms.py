from django import forms
from .models import Veiculo

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class VeiculoAddForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(VeiculoAddForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Veiculo
        fields = ('__all__')
        labels = {

            "contrato": "Contrato",
            "placa": "Placa",
            "situacao": "Situação",
            "statusPlaca": "Status da Placa",
            
        }