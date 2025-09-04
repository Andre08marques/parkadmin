from django.db import models


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
            ("TO", "Tocantins")
)

class Unidade(models.Model):
    nome = models.CharField(max_length=200)
    postalCode = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=100, choices=estado, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    addressNumber = models.CharField(max_length=100, null=True, blank=True)
    vagasLivres = models.IntegerField(default=0)
    vagasPresas = models.IntegerField(default=0)
    horarioFuncionamento = models.TimeField()
    codPessEmpresa = models.CharField(max_length=50, help_text="Sistema externo")
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def endereco_resumido(self):
        """Retorna endereço resumido (rua, número, bairro, cidade)"""
        partes = []
        
        if self.address:
            endereco = self.address
            if self.addressNumber:
                endereco += f", {self.addressNumber}"
            partes.append(endereco)
        
        if self.district:
            partes.append(self.district)
            
        if self.city:
            partes.append(self.city)
        
        return " - ".join(partes) if partes else "Endereço não informado"

