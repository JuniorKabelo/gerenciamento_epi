from django import forms
from .models import Colaborador, Epi, Emprestimo

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'funcao', 'setor']

class EpiForm(forms.ModelForm):
    class Meta:
        model = Epi
        fields = ['nome', 'descricao', 'validade', 'quantidade']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'epi', 'quantidade', 'status']
