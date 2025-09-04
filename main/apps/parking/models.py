from django.db import models

class TabelaPreco(models.Model):
    TIPO_VEICULO_CHOICES = [
        ('carro', 'Carro'),
        ('moto', 'Moto'),
        ('van', 'Van'),
        ('caminhonete', 'Caminhonete'),
    ]
    
    TIPO_PRECO_CHOICES = [
        ('hora', 'Por Hora'),
        ('dia', 'Diária'),
        ('mensal', 'Mensal'),
        ('avulso', 'Avulso'),
    ]

    unidade = models.ForeignKey(
        'core.Unidade', 
        on_delete=models.CASCADE, 
        related_name='tabelas_preco'
    )
    nome = models.CharField(max_length=100, help_text="Nome da tabela de preços")
    tipo_veiculo = models.CharField(max_length=15, choices=TIPO_VEICULO_CHOICES)
    tipo_preco = models.CharField(max_length=10, choices=TIPO_PRECO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tolerancia = models.PositiveIntegerField(
        default=15, 
        help_text="Tolerância em minutos"
    )
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tabela de Preço"
        verbose_name_plural = "Tabelas de Preço"
        unique_together = ['unidade', 'nome', 'tipo_veiculo', 'tipo_preco']

    def __str__(self):
        return f"{self.unidade.nome} - {self.nome} - {self.get_tipo_veiculo_display()} - {self.get_tipo_preco_display()}"