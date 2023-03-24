from django.shortcuts import render, redirect, get_object_or_404
from Empresas.models import Empresa
from usuarios.models import Profile

# Create your views here.


def empresa_detalhe(request, empresa_id):
    
    idUser = request.user.id
    
    empresa = Empresa.objects.filter(id=empresa_id)
    print(empresa)
    profiles = Profile.objects.filter(usuario=idUser)
    processo_a_editar = {
        'profiles':profiles,
        'empresas':empresa
        }
    
    return render(request, 'empresa/empresa.html',processo_a_editar)
