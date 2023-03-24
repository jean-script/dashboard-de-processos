from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from processo.models import Processos
from .models import Profile
from Empresas.models import Empresa
from usuarios.validacao import campo_vazio, senha_nao_sao_iguais

# Create your views here.

#  função de cadastro
def cadastro(request):

    # pap.practia@global.com

    id = request.user.id

    if 'busca_empresa' in request.GET:
        empresas = Empresa.objects.all()
        empresa_pesquisada = request.GET['busca_empresa']
        empresas = Empresa.objects.filter(nome_empresa__icontains=empresa_pesquisada)
    else:
        empresas = Empresa.objects.all()

    profiles = Profile.objects.filter(usuario=id) 

    contexto = {
        'profiles':profiles,
        'empresas':empresas
    }

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        empresa = request.POST.get('empresa_usuario', None)
        admin = request.POST.get('admin', None)

        if admin == 'True':
            admin = True
        else: 
            admin = False

        # validação
        if campo_vazio(nome):
            messages.error(request,'O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request,'O campo e-mail não pode ficar em branco')
            return redirect('cadastro')
        
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar vazios')
            return redirect('cadastro')

        if senha_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senha não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuario já cadastrado')
            
            return redirect('cadastro')     

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuario já cadastrado')
            return redirect('cadastro')   


        empresa_vinculada = Empresa.objects.get(id=empresa)

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        profile_new = Profile.objects.create(empresa=empresa_vinculada,usuario=user,is_admin=admin)
        profile_new.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        print('Usuário cadastrado com sucesso!')
        return redirect('dashboard')

    return render(request, 'usuarios/cadastro.html',contexto)

# função de login
def login(request):

    if request.method == 'POST':
        email = request.POST['Empresa_user']
        senha = request.POST['Empresa_senha']
        print(email, senha)

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar vazios')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                messages.success(request,"Login realizado com sucesso")  
                return redirect('processos')

    return render(request, 'usuarios/login.html')

#  função para fazer o logout
def logout(request):

    auth.logout(request)
    return redirect('login')

# função valida se esta logado e manda para função de processos
def dashboard(request):

    # validando se o usuario esta logado, se não estiver não acessa o dashboard
    if request.user.is_authenticated:
        return redirect('processos')
    else:
        return redirect('login')
        
#  função do perfil do usuario
def perfil(request, user_id):

    # usuario_id = get_object_or_404(User, pk=user_id)
    id = request.user.id
    profiles = Profile.objects.filter(usuario=id) 

    contexto = {
        'profiles':profiles,
    }

    return render(request, 'usuarios/perfil.html',contexto)

# função de criar novos processos
def cria_processo(request):

    id = request.user.id

    if 'busca_empresa' in request.GET:
        empresas = Empresa.objects.all()
        empresa_pesquisada = request.GET['busca_empresa']
        empresas = Empresa.objects.filter(nome_empresa__icontains=empresa_pesquisada)
    else:
        empresas = Empresa.objects.all()

    if 'busca_usuario' in request.GET:
        usuarios = User.objects.all()
        usuario_pesquisada = request.GET['busca_usuario']
        usuarios = User.objects.filter(username__icontains=usuario_pesquisada)
    else:
        usuarios = User.objects.all()

    profiles = Profile.objects.filter(usuario=id) 

    contexto = {
        'usuarios': usuarios,
        'profiles':profiles,
        'empresas':empresas
    }
    usuario_new = []

    if request.method =='POST':
        nome = request.POST['nome_processo']
        descricao = request.POST['descricao']
        status = request.POST['status']
        area = request.POST['area']
        
        usuario_new = request.POST.get('usuario_vin', None)
        empresa = request.POST.get('empresa', None)
        print(empresa)

        if campo_vazio(nome):
            messages.error(request,'O campo nome não pode ficar em branco')
            return redirect('cria_processo')

        if campo_vazio(descricao):
            messages.error(request,'A descrição do processo não pode estar em branco')
            return redirect('cria_processo')

        if usuario_new == 'Selecione um usuário':
            messages.error(request, 'Selecione um usuário cadastrado')
            return redirect('cria_processo')

        # print(usuario_new)
        user = User.objects.get(id=usuario_new)
        empresa_vinculada = Empresa.objects.get(id=empresa) 
        # print(empresa_vinculada)

        processo = Processos.objects.create(
            empresa=empresa_vinculada,
            usuario=user,
            nome_processo=nome,
            descrisao=descricao,
            status=status,
            area=area,
            )

        processo.save()

        
        print("Id do processo: ",processo.id)

        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_processos.html', contexto)

#  função para deletar processos
def deleta_processo(request, processo_id):

    processo = get_object_or_404(Processos, pk=processo_id)

    processo.delete()

    return redirect('dashboard')

# função de ediatar o processo
def edita_processo(request, processo_id):

    id = request.user.id
    empresas = Empresa.objects.all()
    usuarios = User.objects.all()
    profiles = Profile.objects.filter(usuario=id) 

    processo = get_object_or_404(Processos, pk=processo_id)

    processo_a_editar = {
        'processo':processo,
        'usuarios':usuarios,
        'profiles':profiles,
        'empresas':empresas
        }

    return render(request, 'usuarios/edita_processo.html', processo_a_editar)
    
# função atualiza processo
def atualiza_processo(request):

    if request.method == 'POST':
        
        processo_id = request.POST['processo_id']
        p = Processos.objects.get(pk=processo_id)
        p.nome_processo = request.POST['nome_processo']
        p.descrisao = request.POST['descricao']
        p.status = request.POST['status']
        p.area = request.POST['area']
        p.usuario_id = request.POST.get('usuario', None)
        
        if campo_vazio(p.nome_processo):
            messages.error(request, 'O nome do processo não pode estar em branco')
            return redirect('edita_processo',processo_id)

        if campo_vazio(p.descrisao):
            messages.error(request, 'Faça uma descrição do processo')
            return redirect('edita_processo',processo_id)

        if campo_vazio(p.status):
            messages.error(request, 'Informe o status do processo')
            return redirect('edita_processo',processo_id)

        if campo_vazio(p.area):
            messages.error(request, 'Informe a área do processo')
            return redirect('edita_processo',processo_id)

        p.save()
        return redirect('dashboard')
    else:
        return redirect('dashboard')
    
#  função para criar empresa
def cria_empresa(request):

    id = request.user.id
    profiles = Profile.objects.filter(usuario=id) 
    empresas = Empresa.objects.all()

    contexto = {
        'profiles':profiles,
        'empresas':empresas
    }

    if request.method == 'POST':
        nome_empresa = request.POST['nome_empresa']
        
        if 'foto_empresa' in request.FILES:
            foto = request.FILES['foto_empresa']

        if campo_vazio(nome_empresa):
            messages.error(request, 'O campo nome empresa não pode ficar vazio')
            return redirect('cria_empresa')

        

        empresa = Empresa.objects.create(
            nome_empresa=nome_empresa,
            foto_empresa=foto
        )
        empresa.save()

        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_empresa.html', contexto)

# atualiza perfil
def atualiza_perfil(request):

    if request.method == 'POST':
        user_id = request.POST['user_id']
        profile_id = request.POST['profile_id']

        user = User.objects.get(pk=user_id)
        profile = Profile.objects.get(pk=profile_id)

        email_atual = user.email

        user.username = request.POST['username_nome']

        if campo_vazio(user.username):
            messages.error(request, 'O nome do usuário não pode estar em branco')
            return redirect('dashboard')

        user.email = request.POST.get('email', None)

        if user.email == None:
            user.email = email_atual

        if campo_vazio(user.email):
            messages.error(request, 'O E-mail não pode estar em branco')
            return redirect('dashboard')

        user.save()

        profile.cargo = request.POST['cargo']
        profile.endereco = request.POST['endereco']
        profile.telefone = request.POST['telefone']
        profile.cidade = request.POST['cidade']
        profile.estado = request.POST['estado']

        if campo_vazio(profile.cargo):
            messages.error(request, 'O Cargo não pode estar em branco')
            return redirect('perfil',user_id)

        if campo_vazio(profile.endereco):
            messages.error(request, 'O endereço não pode estar em branco')
            return redirect('perfil',user_id)

        if campo_vazio(profile.telefone):
            messages.error(request, 'O Telefone não pode estar em branco')
            return redirect('perfil',user_id)

        if campo_vazio(profile.cidade):
            messages.error(request, 'A Cidade não pode estar em branco')
            return redirect('perfil',user_id)

        if campo_vazio(profile.estado):
            messages.error(request, 'O Estado não pode estar em branco')
            return redirect('perfil',user_id)

        if 'foto_perfil' in request.FILES:
            profile.foto_perfil = request.FILES['foto_perfil']
        
        profile.save()

        return redirect('dashboard')

    else:
        return redirect('perfil')


