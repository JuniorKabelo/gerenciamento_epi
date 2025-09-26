from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


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
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateField(blank=True, null=True)
    quantidade = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Em uso')

    data_prevista_devolucao = models.DateField(blank=True, null=True)
    data_real_devolucao = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.colaborador} - {self.epi} ({self.status})"

    def save(self, *args, **kwargs):
        # Primeiro salva para garantir que data_emprestimo está definida (auto_now_add)
        super().save(*args, **kwargs)

        # Depois define data_prevista_devolucao se não estiver definida
        if not self.data_prevista_devolucao and self.data_emprestimo:
            self.data_prevista_devolucao = (self.data_emprestimo + timedelta(days=30)).date()

            # Salva só esse campo para evitar loop infinito
            super().save(update_fields=['data_prevista_devolucao'])

    def devolvido_antes_do_prazo(self):
        if self.data_real_devolucao and self.data_prevista_devolucao:
            return self.data_real_devolucao < self.data_prevista_devolucao
        return False
