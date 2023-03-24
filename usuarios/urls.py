from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('<int:user_id>/perfil', views.perfil, name='perfil'),
    path('cria/processo', views.cria_processo, name='cria_processo'),
    path('cria/empresa', views.cria_empresa, name='cria_empresa'),
    path('deleta/<int:processo_id>', views.deleta_processo, name='deleta_processo'),
    path('edita/<int:processo_id>', views.edita_processo, name='edita_processo'),
    path('atualiza_processo', views.atualiza_processo, name='atualiza_processo'),
    path('edita/perfil', views.atualiza_perfil, name='atualiza_perfil')
]