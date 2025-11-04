from django.db import models

class TipoVeiculo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tipo de Veículo"
        verbose_name_plural = "Tipos de Veículos"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    STATUS_CHOICES = [
        ('ativa', 'Ativa'),
        ('inativa', 'Inativa'),
    ]

    contrato = models.ForeignKey(
        'customers.Contrato', 
        on_delete=models.CASCADE, 
        related_name='veiculos'
    )
    tipo_veiculo = models.ForeignKey(
        'TipoVeiculo',
        on_delete=models.PROTECT,
        related_name='veiculos',
        verbose_name='Tipo de Veículo',
        null=True,
        blank=True
    )
    placa = models.CharField(max_length=10)
    situacao = models.CharField(max_length=100)
    statusPlaca = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativa')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

    def __str__(self):
        return f"{self.placa} - {self.situacao} ({self.contrato.user.get_full_name()})"

    @property
    def unidade(self):
        return self.contrato.unidade