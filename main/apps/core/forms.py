from django import forms
from django.forms.widgets import TextInput
from .models import Unidade, Patio, Vaga

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
            "cnpj": "CNPJ",
            "postalCode": "CEP",
            "state": "Estado",
            "city": "Cidade",
            "district": "Bairro",
            "address": "Endereço",
            "addressNumber": "Número",
            "vagasLivres": "Vagas livres",
            "vagasPresas": "Vagas presas",
            "vagasManobráveis": "Vagas manobráveis",
            "funciona_feriados": "Funciona em feriados",
            "funciona_segunda": "Segunda-feira",
            "funciona_terca": "Terça-feira",
            "funciona_quarta": "Quarta-feira",
            "funciona_quinta": "Quinta-feira",
            "funciona_sexta": "Sexta-feira",
            "funciona_sabado": "Sábado",
            "funciona_domingo": "Domingo",
            "horario_segunda_inicio": "Início",
            "horario_segunda_fim": "Fim",
            "horario_terca_inicio": "Início",
            "horario_terca_fim": "Fim",
            "horario_quarta_inicio": "Início",
            "horario_quarta_fim": "Fim",
            "horario_quinta_inicio": "Início",
            "horario_quinta_fim": "Fim",
            "horario_sexta_inicio": "Início",
            "horario_sexta_fim": "Fim",
            "horario_sabado_inicio": "Início",
            "horario_sabado_fim": "Fim",
            "horario_domingo_inicio": "Início",
            "horario_domingo_fim": "Fim",
            "codPessEmpresa": "Código da empresa"
        }
        widgets = {
            "cnpj": forms.TextInput(attrs={"class": "form-control"}),
            "horario_segunda_inicio": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_segunda_fim": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_terca_inicio": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_terca_fim": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_quarta_inicio": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_quarta_fim": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_quinta_inicio": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_quinta_fim": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_sexta_inicio": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_sexta_fim": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_sabado_inicio": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_sabado_fim": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_domingo_inicio": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_domingo_fim": forms.TimeInput(attrs={"type": "time", "class": "form-control"})
        }


class PatioForm(forms.ModelForm):
    class Meta:
        model = Patio
        fields = ['nome', 'unidade', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Pátio'}),
            'unidade': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do Pátio', 'rows': 3}),
        }


class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['patio', 'tipo_veiculo', 'quantidade']
        widgets = {
            'patio': forms.Select(attrs={'class': 'form-control'}),
            'tipo_veiculo': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade de Vagas'}),
        }