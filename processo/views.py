from django.shortcuts import render, get_object_or_404, redirect
from .models import Processos, LogsDoProcesso
from django.contrib.auth.models import User
from usuarios.models import Profile
from Empresas.models import Empresa
from datetime import datetime


# Create your views here.

def processos(request):

    if request.user.is_authenticated:

        id = request.user.id
        
        user = request.user
        data_hoje = datetime.now()


        profiles = Profile.objects.filter(usuario=id)
 
        usuarios = User.objects.all()
        empresas = Empresa.objects.all()
        
        
        # validação de super usuario, se for ele pode ver todos os processos
        if user.is_superuser:
            processos = Processos.objects.order_by('-data_publicacao').filter(publicado=True).all()
        else:
            processos = Processos.objects.order_by('-data_publicacao').filter(publicado=True).filter(usuario=id)


        ids_logs = []

        agora = datetime.now()

        data_hoje = agora.strftime('%Y-%m-%d')
        # data = agora.strftime('%d-%m-%Y')
        print(data_hoje)

        for pro in processos:

            id = pro.id
            log_do_processo = LogsDoProcesso.objects.filter(processo_nome=id).filter(data_execucao=data_hoje)
            # print(log_do_processo)
            ids_logs.append(log_do_processo)


        dados_grafico = dados_do_grafico(ids_logs)
        
        print("Dados:",dados_grafico)
        contexto = {
            'processos': processos,
            'profiles':profiles,
            'log_do_processo':ids_logs,
            'usuarios':usuarios,
            'empresas':empresas,
            'dados_grafico':dados_grafico,
        }

        return render(request, 'index.html', contexto)
    else:
        return redirect('login')


def dados(request, processo_id):
    
    id = request.user.id
    profiles = Profile.objects.filter(usuario=id) 
    # obtendo a receita clicada pelo id
    processo = get_object_or_404(Processos, pk=processo_id)

    processo_id = processo.id

    log_do_processo = LogsDoProcesso.objects.filter(processo_nome=processo_id)

    processo_a_exibir = {
        'processo':processo,
        'profiles':profiles,
        'log_do_processo':log_do_processo
    }

    return render(request, 'processo.html', processo_a_exibir)


def dados_do_grafico(logs_processos):

    # declaração de variaveis 
    quantidade_logs = len(logs_processos)
    em_execucao = []
    numero_de_processo_em_execucao = 0
    numero_de_processo_pendentes = 0
    numero_de_processo_finalizados = 0

    status = 'em execucao'.lower()

    for logs in logs_processos:
        
        for f in logs:
            
            processo_em_execucao = f.transaction_status.lower()
            
            if status in processo_em_execucao:
                numero_de_processo_em_execucao += 1
                em_execucao.append(numero_de_processo_em_execucao)
            
            elif processo_em_execucao ==  '':
                numero_de_processo_pendentes += 1
            
            elif len(processo_em_execucao) >= 1:
                numero_de_processo_finalizados += 1
            

    dados_grafico = {
        'quantidade_logs':quantidade_logs,
        'em_execucao':numero_de_processo_em_execucao,
        'pendentes': numero_de_processo_pendentes,
        'finalizados':numero_de_processo_finalizados
    }

    return dados_grafico