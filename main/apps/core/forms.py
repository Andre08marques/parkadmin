from django import forms
from django.forms.widgets import TextInput
from .models import Unidade

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class UnidadeAddform(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = "__all__"
        labels = {
            "nome": "Nome*",
            "postalCode": "Cep",
            "state": "Estado",
            "city": "Cidade",
            "district": "Bairro",
            "address": "Endereço",
            "addressNumber": "Número",
            "vagasLivres": "Vagas livres",
            "horarioAbertura": "Abertura",
            "horarioFechamento": "Fechamento",
            "codPessEmpresa": "Código da empresa"
        }
        widgets = {
            "horarioAbertura": forms.TimeInput(
                attrs={
                    "type": "time",  
                    "class": "form-control"
                }
            ),
            "horarioFechamento": forms.TimeInput(
                attrs={
                    "type": "time",  
                    "class": "form-control"
                }
            )
        }