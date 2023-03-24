from django.urls import path
from . import views

urlpatterns = [
    path('detalhes/<int:empresa_id>', views.empresa_detalhe, name='empresa_detalhe'),
]