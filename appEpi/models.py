from django.db import models
from django.contrib.auth.models import User


class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    funcao = models.CharField(max_length=100, default='Desconhecida')
    setor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Epi(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    validade = models.DateField(blank=True, null=True)
    quantidade = models.PositiveIntegerField(default=0)

    @property
    def quantidade_disponivel(self):
        from .models import Emprestimo
        emprestados = Emprestimo.objects.filter(
            epi=self, status='Em uso'
        ).aggregate(models.Sum('quantidade'))['quantidade__sum'] or 0
        return self.quantidade - emprestados

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('Em uso', 'Em uso'),
        ('Devolvido', 'Devolvido'),
    ]

    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    epi = models.ForeignKey(Epi, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    quantidade = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Em uso')

    def __str__(self):
        return f"{self.colaborador} - {self.epi} ({self.status})"
