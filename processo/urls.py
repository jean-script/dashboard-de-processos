from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.processos, name='processos'),
    path('<int:processo_id>', views.dados, name='dados'),
]