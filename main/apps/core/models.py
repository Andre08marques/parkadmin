from django.db import models
from main.apps.vehicles.models import TipoVeiculo

estado = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
)

dias_semana = (
    ("SEG", "Segunda-feira"),
    ("TER", "Terça-feira"),
    ("QUA", "Quarta-feira"),
    ("QUI", "Quinta-feira"),
    ("SEX", "Sexta-feira"),
    ("SAB", "Sábado"),
    ("DOM", "Domingo"),
)

class Unidade(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome da Unidade",null=True)
    cnpj = models.CharField(max_length=18, verbose_name="CNPJ",null=True)
    codPessEmpresa = models.CharField(max_length=50, verbose_name="Código da Empresa",null=True)
    postalCode = models.CharField(max_length=9, verbose_name="CEP",null=True)
    state = models.CharField(max_length=2, choices=estado, verbose_name="Estado",null=True)
    city = models.CharField(max_length=100, verbose_name="Cidade",null=True)
    district = models.CharField(max_length=100, verbose_name="Bairro",null=True)
    address = models.CharField(max_length=200, verbose_name="Endereço",null=True)
    addressNumber = models.CharField(max_length=10, verbose_name="Número",null=True)
    funciona_feriados = models.BooleanField(default=False, verbose_name="Funciona em Feriados")
    funciona_segunda = models.BooleanField(default=False, verbose_name="Funciona Segunda-feira")
    horario_segunda_inicio = models.TimeField(null=True, blank=True, verbose_name="Início Segunda-feira")
    horario_segunda_fim = models.TimeField(null=True, blank=True, verbose_name="Fim Segunda-feira")
    funciona_terca = models.BooleanField(default=False, verbose_name="Funciona Terça-feira")
    horario_terca_inicio = models.TimeField(null=True, blank=True, verbose_name="Início Terça-feira")
    horario_terca_fim = models.TimeField(null=True, blank=True, verbose_name="Fim Terça-feira")
    funciona_quarta = models.BooleanField(default=False, verbose_name="Funciona Quarta-feira")
    horario_quarta_inicio = models.TimeField(null=True, blank=True, verbose_name="Início Quarta-feira")
    horario_quarta_fim = models.TimeField(null=True, blank=True, verbose_name="Fim Quarta-feira")
    funciona_quinta = models.BooleanField(default=False, verbose_name="Funciona Quinta-feira")
    horario_quinta_inicio = models.TimeField(null=True, blank=True, verbose_name="Início Quinta-feira")
    horario_quinta_fim = models.TimeField(null=True, blank=True, verbose_name="Fim Quinta-feira")
    funciona_sexta = models.BooleanField(default=False, verbose_name="Funciona Sexta-feira")
    horario_sexta_inicio = models.TimeField(null=True, blank=True, verbose_name="Início Sexta-feira")
    horario_sexta_fim = models.TimeField(null=True, blank=True, verbose_name="Fim Sexta-feira")
    funciona_sabado = models.BooleanField(default=False, verbose_name="Funciona Sábado")
    horario_sabado_inicio = models.TimeField(null=True, blank=True, verbose_name="Início Sábado")
    horario_sabado_fim = models.TimeField(null=True, blank=True, verbose_name="Fim Sábado")
    funciona_domingo = models.BooleanField(default=False, verbose_name="Funciona Domingo")
    horario_domingo_inicio = models.TimeField(null=True, blank=True, verbose_name="Início Domingo")
    horario_domingo_fim = models.TimeField(null=True, blank=True, verbose_name="Fim Domingo")

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"

    def __str__(self):
        return self.nome

class Patio(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Pátio")
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="patios", verbose_name="Unidade")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    class Meta:
        verbose_name = "Pátio"
        verbose_name_plural = "Pátios"

    def __str__(self):
        return f"{self.nome} - {self.unidade.nome}"

class Vaga(models.Model):
    patio = models.ForeignKey(Patio, on_delete=models.CASCADE, related_name="vagas", verbose_name="Pátio")
    tipo_veiculo = models.ForeignKey(TipoVeiculo, on_delete=models.CASCADE, verbose_name="Tipo de Veículo")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade de Vagas")

    class Meta:
        verbose_name = "Vaga"
        verbose_name_plural = "Vagas"

    def __str__(self):
        return f"{self.quantidade} vagas para {self.tipo_veiculo.nome} no {self.patio.nome}"