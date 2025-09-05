from django import forms
from django.forms.widgets import TextInput
from .models import TabelaPreco

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class TablePriceAddform(FormSettings):
    def __init__(self, *args, **kwargs):
        super(TablePriceAddform, self).__init__(*args, **kwargs)

    class Meta:
        model = TabelaPreco
        fields = ('__all__')
        labels = {
           "nome": "Nome*",
           "postalCode": "Cep",
           "state": "Estado",
           "city": "Cidade",
           "district": "Bairro",
           "address": "Endereço",
           "addressNumber": "Número",
           "vagasLivres": "Vagas livres",
           "horarioFuncionamento": "Horário de funcionamento",
           "codPessEmpresa": "Código da empresa"

        }