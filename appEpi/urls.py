from django.urls import path
from . import views

urlpatterns = [
    # Home (Dashboard principal)
    path('', views.home, name='home'),

    # Login / Logout
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Colaboradores
    path('colaboradores/', views.listar_colaboradores, name='listar_colaboradores'),
    path('colaboradores/cadastrar/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('colaboradores/editar/<int:id>/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/excluir/<int:id>/', views.excluir_colaborador, name='excluir_colaborador'),

    # EPIs
    path('epis/', views.listar_epis, name='listar_epis'),
    path('epis/cadastrar/', views.cadastrar_epi, name='cadastrar_epi'),
    path('epis/editar/<int:id>/', views.editar_epi, name='editar_epi'),
    path('epis/excluir/<int:id>/', views.excluir_epi, name='excluir_epi'),

    # Empréstimos
    path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
    path('emprestimos/registrar/', views.registrar_emprestimo, name='registrar_emprestimo'),
    path('emprestimos/devolver/<int:id>/', views.registrar_devolucao, name='registrar_devolucao'),

    # URL para os empréstimos de cada colaborador (corrigido)
    path('colaboradores/<int:colaborador_id>/emprestimos/', views.listar_emprestimos_colaborador, name='listar_emprestimos_colaborador'),
]
