from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Colaborador, Epi, Emprestimo
from .forms import ColaboradorForm, EpiForm, EmprestimoForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    total_colaboradores = Colaborador.objects.count()
    total_epis = Epi.objects.count()
    epis_em_uso = Emprestimo.objects.filter(status='Em uso').count()
    ultimos_emprestimos = Emprestimo.objects.order_by('-data_emprestimo')[:5]

    context = {
        'total_colaboradores': total_colaboradores,
        'total_epis': total_epis,
        'epis_em_uso': epis_em_uso,
        'ultimos_emprestimos': ultimos_emprestimos,
        'usuario': request.user,
    }
    return render(request, 'home.html', context)

# Listar colaboradores
@login_required
def listar_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores/listar.html', {'colaboradores': colaboradores})

# Cadastrar colaborador
@login_required
def cadastrar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_colaboradores')
    else:
        form = ColaboradorForm()
    return render(request, 'colaboradores/cadastrar.html', {'form': form})

# Editar colaborador
@login_required
def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('listar_colaboradores')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'colaboradores/editar.html', {'form': form})

# Excluir colaborador
@login_required
def excluir_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        colaborador.delete()
        return redirect('listar_colaboradores')
    return render(request, 'colaboradores/excluir.html', {'colaborador': colaborador})

# Similar para EPIs:

@login_required
def listar_epis(request):
    epis = Epi.objects.all()
    return render(request, 'epis/listar.html', {'epis': epis})

@login_required
def cadastrar_epi(request):
    if request.method == 'POST':
        form = EpiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_epis')
    else:
        form = EpiForm()
    return render(request, 'epis/cadastrar.html', {'form': form})

@login_required
def editar_epi(request, id):
    epi = get_object_or_404(Epi, id=id)
    if request.method == 'POST':
        form = EpiForm(request.POST, instance=epi)
        if form.is_valid():
            form.save()
            return redirect('listar_epis')
    else:
        form = EpiForm(instance=epi)
    return render(request, 'epis/editar.html', {'form': form})

@login_required
def excluir_epi(request, id):
    epi = get_object_or_404(Epi, id=id)
    if request.method == 'POST':
        epi.delete()
        return redirect('listar_epis')
    return render(request, 'epis/excluir.html', {'epi': epi})
@login_required
def home(request):
    total_colaboradores = Colaborador.objects.count()
    total_epis = Epi.objects.count()
    emprestimos = Emprestimo.objects.all().order_by('-data_emprestimo')[:5]  # últimos 5 empréstimos
    return render(request, 'home.html', {
        'total_colaboradores': total_colaboradores,
        'total_epis': total_epis,
        'emprestimos': emprestimos,
    })
# EMPRESTIMOS
@login_required
def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.select_related('colaborador', 'epi').all()
    return render(request, 'emprestimos/listar.html', {'emprestimos': emprestimos})

@login_required
def registrar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            if emprestimo.quantidade <= emprestimo.epi.quantidade:
                emprestimo.epi.quantidade -= emprestimo.quantidade
                emprestimo.epi.save()
                emprestimo.save()
                return redirect('listar_emprestimos')
            else:
                form.add_error('quantidade', 'Quantidade maior que o estoque disponível.')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimos/cadastrar.html', {'form': form})

@login_required
def registrar_devolucao(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == 'POST':
        if emprestimo.status == 'Em uso':
            emprestimo.status = 'Devolvido'
            emprestimo.epi.quantidade += emprestimo.quantidade
            emprestimo.epi.save()
            emprestimo.save()
        return redirect('listar_emprestimos')
    return render(request, 'emprestimos/devolver.html', {'emprestimo': emprestimo})
