from django import forms
from .models import Colaborador, Epi, Emprestimo

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'funcao', 'setor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'funcao': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'setor': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
        }

class EpiForm(forms.ModelForm):
    class Meta:
        model = Epi
        fields = ['nome', 'descricao', 'validade', 'quantidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'validade': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width: 300px;'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'epi', 'quantidade', 'status']
        widgets = {
            'colaborador': forms.Select(attrs={'class': 'form-select', 'style': 'width: 300px;'}),
            'epi': forms.Select(attrs={'class': 'form-select', 'style': 'width: 300px;'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'status': forms.Select(attrs={'class': 'form-select', 'style': 'width: 300px;'}),
        }
