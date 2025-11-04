from django.db import models
from main.apps.core.models import Unidade



class TabelaPreco(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="tabelas_preco")
    nome = models.CharField(max_length=100)
    ativa = models.BooleanField(default=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.unidade.nome}"


class TipoVeiculo(models.Model):
    nome = models.CharField(max_length=50)  # Ex: Moto, Carro, Caminhão, Van
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class TipoCobranca(models.Model):
    nome = models.CharField(max_length=50)  # Ex: Hora, Diária, Contrato Mensal
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Preco(models.Model):
    tabela = models.ForeignKey(TabelaPreco, on_delete=models.CASCADE, related_name="precos")
    tipo_veiculo = models.ForeignKey(TipoVeiculo, on_delete=models.CASCADE)
    tipo_cobranca = models.ForeignKey(TipoCobranca, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('tabela', 'tipo_veiculo', 'tipo_cobranca')

    def __str__(self):
        return f"{self.tabela.nome} - {self.tipo_veiculo} ({self.tipo_cobranca}): R${self.valor}"