from django import forms
from .models import Contrato

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class ContratoAddForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(ContratoAddForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Contrato
        fields = ('__all__')
        labels = {

            "user": "Usuário*",
            "unidade": "Unidade*",
            "status": "Status",
            "quantidadePlacas": "Quantidade de Placas",
            "placasSimultaneas": "Placas Simultaneas",
            "diaVencimento": "Dia de Vencimento",
            "tipoPagamento": "Tipo de Pagamento",
            "tipoFaturamento": "Tipo de Faturamento",
            
        }