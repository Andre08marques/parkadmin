from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TIPO_CHOICES = [
        ('admin', 'Administrador'),
        ('funcionario', 'Funcionário'),
        ('cliente', 'Cliente'),
    ]
    
    unidade = models.ForeignKey(
        'core.Unidade', 
        on_delete=models.CASCADE, 
        related_name='usuarios'
    )
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES, default='funcionario')
    telefone = models.CharField(max_length=20, blank=True)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f"{self.get_full_name()} - {self.unidade.nome}"
