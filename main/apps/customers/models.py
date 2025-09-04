from django.db import models

class Contrato(models.Model):
    TIPO_PAGAMENTO_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('cartao', 'Cartão'),
        ('pix', 'PIX'),
        ('boleto', 'Boleto'),
    ]
    
    TIPO_FATURAMENTO_CHOICES = [
        ('nfs', 'Nota Fiscal de Serviço'),
        ('recibo', 'Recibo'),
    ]

    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='contratos'
    )
    unidade = models.ForeignKey(
        'core.Unidade', 
        on_delete=models.CASCADE, 
        related_name='contratos'
    )
    status = models.CharField(max_length=50)
    quantidadePlacas = models.IntegerField()
    placasSimultaneas = models.IntegerField()
    diaVencimento = models.IntegerField()
    tipoPagamento = models.CharField(max_length=20, choices=TIPO_PAGAMENTO_CHOICES)
    tipoFaturamento = models.CharField(max_length=10, choices=TIPO_FATURAMENTO_CHOICES)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

    def __str__(self):
        return f"Contrato {self.id} - {self.user.get_full_name()} - {self.unidade.nome}"